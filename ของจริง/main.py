import imutils
import cv2
import numpy as np
import mapper

img = cv2.imread('test1.jpg')
imS = cv2.resize(img, (500, 470))

gray = cv2.cvtColor(imS, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)[1]


# corners = cv2.goodFeaturesToTrack(thresh, 4 ,0.01,100)
# corners = np.int0(corners)
# for corner in corners:
#     x,y = corner.ravel()
#     cv2.circle(imS,(x,y),3,(255,0,0),-1)

edged = cv2.Canny(thresh, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
    epsilon = 0.06 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    # cv2.drawContours(thresh, [approx], 0, (255, 255, 255), 2)

    print(approx)


# for c in cnts: #1
#  # find bounding box coordinates
#  x,y,w,h = cv2.boundingRect(c)
#  print(x)
#  print(y)
#  print(w)
#  print(h)
# cv2.rectangle(imS, (x,y), (x+w, y+h), (0, 255, 0), 2)
# # find minimum area
# rect = cv2.minAreaRect(c)
# # calculate 4 coordinates of the minimum area rectangle
# box = cv2.boxPoints(rect)
# print(box)
# # casting to integers
# box = np.int64(box) #6
#  # draw contours
# cv2.drawContours(imS, [box], 0, (0,0, 255), 2)
myPoints = np.array(approx,dtype=np.int32)
print('********************************')
print(myPoints)

w = 2480; h = 3508;
pts1 = np.float32([myPoints[2], myPoints[4], myPoints[1], myPoints[0]])
pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(imS, matrix, (w, h))
cv2.imwrite('result.jpg',result)


gray1 = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
blurred1 = cv2.GaussianBlur(gray1, (5, 5), 0)
thresh1 = cv2.threshold(blurred1, 150, 255, cv2.THRESH_BINARY)[1]

edged1 = cv2.Canny(thresh1, 50, 100)
edged1 = cv2.dilate(edged1, None, iterations=1)
edged1 = cv2.erode(edged1, None, iterations=1)

cnts = cv2.findContours(edged1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:

    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 10)


cv2.imwrite('resultFeet.jpg',result)
print(x)
print(y)
print(w)
print(h)

WF = (w*11.81)/100
WH = (h*11.81)/100
print(WF)
print(WH)
# cv2.imshow("Scanned", result)
 # press q or Esc to close
# cv2.waitKey(0)
# cv2.destroyAllWindows()
