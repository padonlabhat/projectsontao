import cvzone
import cv2
import numpy as np

imgBack = cv2.imread("background.jpg")
# imgFront = cv2.imread("cup.png", cv2.IMREAD_UNCHANGED)
# imgFront = cv2.resize(imgFront,(0,0),None,0.1,0.1)

imgFront = cv2.imread("cup.png")
imgBack[0:860,0:1151] = imgFront

# imgResult = cvzone.overlayPNG(imgBack, imgFront, [100,100])
# cv2.imshow("Image", imgResult)

# cv2.imshow("Image", imgFront)
cv2.imshow("Image", imgBack)
cv2.waitKey(0)