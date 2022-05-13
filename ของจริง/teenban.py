import cv2

def preImg():
    img = cv2.resize(cv2.imread('img teenban/input/IMG_1248.jpg'), (800, 800))
    cv2.imshow('img', img)
    cv2.waitKey(0)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('img', thresh1)
    cv2.waitKey(0)
preImg()
