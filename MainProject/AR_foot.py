import torch
import cv2
import os
import cvzone
from vedo import *
import vedo
def overlayImg(pathBack,pathFront,sizeImg,location):
    location = [int(location[0]-sizeImg/2),int(location[1]-sizeImg/2)]
    imgBack = pathBack
    imgFront = cv2.imread(pathFront, cv2.IMREAD_UNCHANGED)
    imgFront = cv2.resize(imgFront,(sizeImg,sizeImg))
    imgResult = cvzone.overlayPNG(imgBack, imgFront, location)
    return imgResult

def AR_by_video(camera,pathModel):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=pathModel)
    cap = cv2.VideoCapture(camera)
    while True:
        _, frame = cap.read()
        results = model(frame)
        # results.render()
        testlocation = results.pandas().xyxy[0]
        # print(results.pandas().xyxy[0])
        print(testlocation)
        # print('Xmax',testlocation.xmax[0])
        print(testlocation.empty)
        print('************')


        if testlocation.empty == False :
            x1, y1 = testlocation.xmin[0], testlocation.ymin[0]
            x2, y2 = testlocation.xmax[0], testlocation.ymax[0]
            (x, y) = (x2 + x1) / 2, (y2 + y1) / 2
            print('center point : ', x, y)
            frame = cv2.circle(frame, (int(x), int(y)), radius=0, color=(0, 0, 255), thickness=10)
            if (x2-x1)<(y2-y1):
                sizeImg = int(x2-x1)
            else :
                sizeImg = int(y2-y1)
            sizeImg = 200
            location = [int(x), int(y)]
            set3Dobj(mesh, angle=90,way=(1, 0, 0),screenshot=True)
            imgResult = overlayImg(frame,'output/shoes.png',sizeImg,location)
            set3Dobj(mesh, angle=-90,way=(1, 0, 0),screenshot=False)
            frame = cv2.circle(imgResult, (int(x), int(y)), radius=0, color=(0, 0, 255), thickness=10)
        key = cv2.waitKey(1)
        if key == ord('c'):
            cv2.destroyAllWindows()
            break
        results.render()
        cv2.imshow('preview-frame',frame)
def read3DObj(pathObj,pathDesign):
    mesh = Mesh(pathObj)
    mesh.texture(pathDesign, scale=1)
    return mesh

def set3Dobj(mesh,angle,way,screenshot=False):
    settings.screenshotTransparentBackground = True
    mesh.rotate(angle, axis=way, point=(0, 0, 0), rad=False)
    # mesh.show()
    plotter = vedo.Plotter(offscreen=True)
    plotter += mesh
    if screenshot == True :
        plotter.show().screenshot('output/shoes.png')

mesh = read3DObj("data/AR/supastarOBJ.obj","data/AR/cup.png")
AR_by_video(2,'my models/best_footA4.pt')











# read3DObj("data/AR/supastarOBJ.obj","data/AR/cup.png",90,(1, 0, 0))