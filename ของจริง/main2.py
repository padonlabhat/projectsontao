import cv2
import imutils
import numpy as np

def take_a_photo():
    cap = cv2.VideoCapture(1)
    # cap = cv2.VideoCapture('rtsp://192.168.100.192:8080/h264_pcm.sdp')
    while True:
        _, frame = cap.read()
        frame = cv2.resize(frame, (800, 800))
        # w = frame.shape[0]
        # h = frame.shape[1]
        start_point =(200,100)
        end_point =(500,600)
        frame = cv2.rectangle(frame, start_point, end_point, (0,0,255), 2)
        cv2.imshow('frame',frame)
        key = cv2.waitKey(1)
        if key == ord('c'):
            cropped_image = frame[100:600, 200:500]
            # cv2.imshow('frame', cropped_image)
            cv2.imwrite('capture.png',cropped_image)

            cv2.destroyAllWindows()
            break
take_a_photo()

# pts1 = []
# pts2 = [[0, 0], [2480, 0], [2480, 3508], [0, 3508]]
# def onClick(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         if len(pts1) < 4:
#             pts1.append([x, y])
#             print(pts1)
# img = cv2.imread('test1.jpg')  #****************************ชื่อรูป**************************
# imS= cv2.resize(img, (800, 800))
# cv2.imshow("test1", imS)
# # cv2.namedWindow('frame')
# cv2.setMouseCallback('test1', onClick)
# cv2.waitKey(0)
#
# if len(pts1) == 4:
#
#     T = cv2.getPerspectiveTransform(np.float32(pts1), np.float32(pts2))
#
#     result = cv2.warpPerspective(imS, T, (2480, 3508))
#     # w = 2480;
#     # h = 3508;
#     # pts1 = np.float32([myPoints[2], myPoints[4], myPoints[1], myPoints[0]])
#     # pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
#     # matrix = cv2.getPerspectiveTransform(pts1, pts2)
#     # result = cv2.warpPerspective(imS, matrix, (w, h))
#
# cv2.imshow('frame', result)
# cv2.waitKey(0)
# cv2.imwrite('savedImage.jpg', result)
#
# gray1 = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
# blurred1 = cv2.GaussianBlur(gray1, (5, 5), 0)
# thresh1 = cv2.threshold(blurred1, 150, 255, cv2.THRESH_BINARY)[1]
#
# edged1 = cv2.Canny(thresh1, 50, 100)
# edged1 = cv2.dilate(edged1, None, iterations=1)
# edged1 = cv2.erode(edged1, None, iterations=1)
#
# cnts = cv2.findContours(edged1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
#
# for c in cnts:
#
#     x, y, w1, h1 = cv2.boundingRect(c)
#     cv2.rectangle(result, (x, y), (x + w1, y + h1), (0, 255, 0), 10)
#
#
# cv2.imwrite('output/7edgedFeet.jpg',result)
# result= cv2.resize(result, (800, 800))
# cv2.imshow('frame', result)
# cv2.waitKey(0)
# print(x)
# print(y)
# print(w1)
# print(h1)
#
# WF = (w1/11.81)/10
# WH = (h1/11.81)/10
# print(WF)
# print(WH)

