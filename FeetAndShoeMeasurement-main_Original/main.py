from sklearn.cluster import KMeans
import random as rng
import cv2
import imutils
import argparse
from imutils import contours
from skimage.io import imread
import numpy as np
import matplotlib.pyplot as plt
import os

from utils import *


ImgPath = 'data/barefeet1.jpeg'




def main():

    #import รูปภาพ
    img = imread(ImgPath)
    print(" 1 import รูปภาพ ")
    plt.imshow(img[:,:,::1])
    plt.show()

    if not os.path.exists('output'):
        os.makedirs('output')

    #HSV filter
    print(" 2 ใส่ HSV filter")
    preprocessedOimg = preprocess(img)
    cv2.imwrite('output/preprocessedOimg.jpg', preprocessedOimg)
    plt.imshow(preprocessedOimg[:,:,::1])
    plt.show()

    #
    print(" 3 ")
    clusteredImg = kMeans_cluster(preprocessedOimg)
    cv2.imwrite('output/clusteredImg.jpg', clusteredImg)
    print(clusteredImg)
    plt.imshow(clusteredImg[:,:,::1])
    plt.show()

    #
    print(" 4 ")
    edgedImg = edgeDetection(clusteredImg)
    cv2.imwrite('output/edgedImg.jpg', edgedImg)
    print(edgedImg)
    # plt.imshow(edgedImg[:,:,::1])
    # plt.show()

    #
    print(" 5 ")
    boundRect, contours, contours_poly, img = getBoundingBox(edgedImg)
    pdraw = drawCnt(boundRect[1], contours, contours_poly, img)
    cv2.imwrite('output/pdraw.jpg', pdraw)
    plt.imshow(pdraw[:,:,::1])
    plt.show()

    # วัดขนาดรูปภาพและมุม
    print(" 6 วัดขนาดรูปภาพและมุม ")
    croppedImg, pcropedImg = cropOrig(boundRect[1], clusteredImg)
    # print(" 66 ")
    cv2.imwrite('output/croppedImg.jpg', croppedImg)
    # print(" 666 ")
    plt.imshow(croppedImg[:,:,::1])
    plt.show()

    #สร้างรูปภาพใหม่
    print(" 7 สร้างรูปภาพใหม่ ")
    newImg = overlayImage(croppedImg, pcropedImg)
    cv2.imwrite('output/newImg.jpg', newImg)
    plt.imshow(newImg[:,:,::1])
    plt.show()

    #วัดไซต์ให้ถูกต้อง
    print(" 8 วัดไซต์ให้ถูกต้อง ")
    fedged = edgeDetection(newImg)
    fboundRect, fcnt, fcntpoly, fimg = getBoundingBox(fedged)
    fdraw = drawCnt(fboundRect[2], fcnt, fcntpoly, fimg)
    cv2.imwrite('output/fdraw.jpg', fdraw)
    plt.imshow(fdraw[:,:,::1])
    plt.show()

    #คำนวณไซต์เท้า
    print(" 9 คำนวณไซต์เท้า ")
    print("feet size (cm): ", calcFeetSize(pcropedImg, fboundRect)/10)


if __name__ == '__main__':
    main()