import cv2
import imutils
import numpy
import numpy as np
import matplotlib.pyplot as plt
def take_a_photo():
    # cap = cv2.VideoCapture(1)
    cap = cv2.VideoCapture('rtsp://192.168.1.120:8080/h264_pcm.sdp')
    while True:
        _, frame = cap.read()

        frame = cv2.resize(frame, (800, 800))
        # w = frame.shape[0]
        # h = frame.shape[1]
        start_point =(100,150)
        end_point =(700,650)
        frame = cv2.rectangle(frame, start_point, end_point, (0,0,255), 2)
        cv2.imshow('frame',frame)
        key = cv2.waitKey(1)
        if key == ord('c'):
            cropped_image = frame[150:650, 100:700]
            # cv2.imshow('frame', cropped_image)
            cv2.imwrite('capture.jpg',cropped_image)

            cv2.destroyAllWindows()
            break

def findA4():
    img = cv2.resize(cv2.imread('test4.jpg'), (800, 800))
    cv2.imshow('img', img)
    cv2.waitKey(0)

    # lower = numpy.array([150,150,150])
    # upper = numpy.array([255,255,255])
    mask_a4 = cv2.inRange(img,numpy.array([150,150,150]),numpy.array([255,255,255]))
    cv2.imshow('mask_a4', mask_a4)
    cv2.waitKey(0)
    kernel = np.ones((10, 10), np.uint8)
    mask_a4 = cv2.dilate(mask_a4, kernel, iterations=1)
    mask_a4 = cv2.erode(mask_a4, kernel, iterations=1)

    cv2.imshow('mask_a4', mask_a4)
    cv2.waitKey(0)

    cnts = cv2.findContours(mask_a4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        epsilon = 0.06 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)
        # contourSS = cv2.drawContours(img, [approx], 0, (0, 255,0), 2)
        # print(approx)

    myPoints = np.array(approx, dtype=np.int32)
    print('********************************')
    print(myPoints)
    print('********************************')


    cv2.imshow('img', img)
    # plt.imshow(img)
    # plt.show()
    cv2.waitKey(0)

    w =620;
    h = 877;
    point0=myPoints[0]
    point1 = myPoints[1]
    point4 = myPoints[4]
    # print('********************************')
    # print('P0 = ',point0)
    # print('P1 = ', point1)
    # print('P4 = ', point4)
    point0 = point0[0]
    point1 = point1[0]
    point4 = point4[0]
    # print('P0 = ', point0)
    # print('P1 = ', point1)
    # print('P4 = ', point4)
    XP0 = point0[0]
    XP1 = point1[0]
    XP4 = point4[0]

    YP1 = point1[1]
    YP4 = point4[1]
    # print('XP0 = ', XP0)
    # print('XP1 = ', XP1)
    # print('XP4 = ', XP4)
    # print('YP1 = ', YP1)
    # print('YP4 = ', YP4)

    if XP0>XP1 and YP1<YP4 :
        pts1 = np.float32([myPoints[1], myPoints[0], myPoints[2], myPoints[4]])
    else :
        pts1 = np.float32([myPoints[0], myPoints[4], myPoints[1], myPoints[3]])

    pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(img, matrix, (w, h))
    cv2.imshow('img', result)
    cv2.waitKey(0)
# take_a_photo()
# findA4()


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

