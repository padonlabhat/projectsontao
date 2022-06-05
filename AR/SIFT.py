import cv2
import numpy as np
from vedo import *

# IM = cv2.imread('Doraemon.jpg')
IM = Mesh("data/10055_Gray_Wolf_v1_L3.obj",)
IM.texture("data/10055_Gray_Wolf_Diffuse_v1.jpg", scale=0.1)
AR = cv2.imread("data/qr.png", cv2.IMREAD_GRAYSCALE)

IM = cv2.resize(IM, AR.shape)
sift = cv2.SIFT_create()
matcher = cv2.FlannBasedMatcher(dict(algorithm=1, trees=5), dict(checks=50))
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
kp1, des1 = sift.detectAndCompute(AR, None)
while True:
    rect, frame = cap.read()
    img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp2, des2 = sift.detectAndCompute(img2, None)
    matched = matcher.knnMatch(des1, des2, k=2)
    good = []
    for m, n in matched:
        if m.distance < 0.6 * n.distance:
            good.append(m)
    if len(good) >= 4:
        # M = cv2.drawMatches(AR, kp1, img2, kp2, good, None, flags=2)
        # cv2.imshow('M', M)
        pt1 = np.float32([kp1[m.queryIdx].pt for m in good])
        pt2 = np.float32([kp2[m.trainIdx].pt for m in good])
        T1, _ = cv2.findHomography(pt2, pt1, cv2.RANSAC, 5.0)
        if T1 is not None:
            img3 = cv2.warpPerspective(img2, T1, AR.shape)
            cv2.imshow('img3', img3)
        T2, _ = cv2.findHomography(pt1, pt2, cv2.RANSAC, 5.0)
        if T2 is not None:
            mask = cv2.warpPerspective(np.ones_like(AR, dtype=np.uint8),
                                       T2, (frame.shape[1], frame.shape[0]))
            mask = ((mask > 0) * 255).astype(np.uint8)
            mask_inv = cv2.bitwise_not(mask)
            bg = cv2.bitwise_and(frame, frame, mask=mask_inv)
            obj = cv2.warpPerspective(IM,
                                       T2, (frame.shape[1], frame.shape[0]))
            fg = cv2.bitwise_and(obj, obj, mask=mask)
            frame = cv2.add(fg, bg)
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
