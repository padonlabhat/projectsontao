import torch
import cv2
import os
import cvzone
from vedo import *
import vedo
from PIL import Image
def overlayImg(pathBack,pathFront,sizeImg,location):
    location = [int(location[0]-sizeImg/2),int(location[1]-sizeImg/2)]
    imgBack = pathBack
    imgFront = cv2.imread(pathFront, cv2.IMREAD_UNCHANGED)
    imgFront = cv2.resize(imgFront,(sizeImg,sizeImg))
    imgResult = cvzone.overlayPNG(imgBack, imgFront, location)
    return imgResult
def cropimg(pathImg):
    im = Image.open(pathImg)
    im.size
    im.getbbox()
    im2 = im.crop(im.getbbox())
    im2.size
    im2.save('output/crop_shoes.png')

def AR_by_video(camera,pathModel):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=pathModel)
    cap = cv2.VideoCapture(camera)
    while True:
        _, frame = cap.read()
        results = model(frame)
        results.render()
        testlocation = results.pandas().xyxy[0]
        # print(results.pandas().xyxy[0])
        print(testlocation)
        # print('Xmax',testlocation.xmax[0])
        print(testlocation.empty)
        print('************')


        if testlocation.empty == False :
            xmin, ymin = testlocation.xmin[0], testlocation.ymin[0]
            xmax, ymax = testlocation.xmax[0], testlocation.ymax[0]
            (x, y) = (xmax + xmin) / 2, (ymax + ymin) / 2
            print('center point : ', x, y)
            frame = cv2.circle(frame, (int(x), int(y)), radius=0, color=(0, 0, 255), thickness=10)
            if (xmax-xmin)<(ymax-ymin):
                sizeImg = int(xmax-xmin)
            else :
                sizeImg = int(ymax-ymin)
            # width = int(xmax-xmin)
            # long = int(ymax-ymin)
            # sizeImg = (width,long)
            location = [int(x), int(y)]
            # imgResult = set3Drighttop(frame,sizeImg,location)
            imgResult = set3Dleft(frame,sizeImg,location)
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

def set3Dstraighttop(frame,sizeImg,location,angle=90):
    set3Dobj(mesh, angle=angle, way=(1, 0, 0), screenshot=True)
    imgResult = overlayImg(frame, 'output/shoes.png', sizeImg, location)
    set3Dobj(mesh, angle=-angle, way=(1, 0, 0), screenshot=False)
    return imgResult

def set3Dlefttop(frame,sizeImg,location,angle=45):
    set3Dobj(mesh, angle=90,way=(1, 0, 0))
    way=(1, 0, 1)
    set3Dobj(mesh, angle=angle,way=way,screenshot=True)
    imgResult = overlayImg(frame,'output/shoes.png',sizeImg,location)
    set3Dobj(mesh, angle=-angle, way=way)
    set3Dobj(mesh, angle=-90,way=(1, 0, 0))
    return imgResult

def set3Drighttop(frame,sizeImg,location,angle=45):
    set3Dobj(mesh, angle=90,way=(1, 0, 0))
    way=(-1, 0, -1)
    set3Dobj(mesh, angle=angle,way=way,screenshot=True)
    imgResult = overlayImg(frame,'output/shoes.png',sizeImg,location)
    set3Dobj(mesh, angle=-angle, way=way)
    set3Dobj(mesh, angle=-90,way=(1, 0, 0))
    return imgResult

def set3Drigh(frame,sizeImg,location,angle=270):
    way=(1, 45, 0)
    set3Dobj(mesh, angle=angle,way=way,screenshot=True)
    imgResult = overlayImg(frame,'output/shoes.png',sizeImg,location)
    set3Dobj(mesh, angle=-angle, way=way)

    return imgResult

def set3Dleft(frame,sizeImg,location,angle=90):
    way=(1, 45, 0)
    set3Dobj(mesh, angle=angle,way=way,screenshot=True)
    cropimg('output/shoes.png')
    imgResult = overlayImg(frame,'output/crop_shoes.png',sizeImg,location)
    set3Dobj(mesh, angle=-angle, way=way)
    return imgResult

# mesh = read3DObj("data/AR/supastarOBJ.obj","data/AR/cup.png")
# set3Dobj(mesh, angle=90,way=(1, 0, 0),screenshot=True)
# for i in range(45):
#     way = (-1, 0, -1)
#     set3Dobj(mesh, angle=i,way=way,screenshot=True)
#     set3Dobj(mesh, angle=-i, way=way)
#     frame = cv2.imread('output/shoes.png')
#     cv2.imshow('preview-frame', frame)
#     cv2.waitKey(1)

# frame = cv2.imread('output/shoes.png')
# cv2.imshow('preview-frame', frame)
# cv2.waitKey(1)


def get_location_to_list(len_list):
    list = []
    for i in range(len(testlocation.name)) :
        detail =[]
        detail.append(testlocation.name[i])
        detail.append(testlocation.xmin[i])
        detail.append(testlocation.ymin[i])
        detail.append(testlocation.xmax[i])
        detail.append(testlocation.ymax[i])
        list.append(detail)
    return list

def find_xy_from_class(list,name) :
    index_name = []
    for i in range(len(list)):
        if list[i][0] == name:
            print('index ',i,' ',name)
        index_name.append(i)
    print(len(index_name))
    xmin = list[i][1]
    ymin = list[i][2]
    xmax =list[i][3]
    ymax = list[i][4]

    return xmin,ymin,xmax,ymax

# frame = 'input/ggg.png'
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='my models/best_footA4.pt')
# results = model(frame)
# testlocation = results.pandas().xyxy[0]
# print(get_location_to_list(testlocation))
# print(find_xy_from_class(get_location_to_list(testlocation),'Foot on A4'))


# mesh = read3DObj("data/AR/supastarOBJ.obj","data/AR/cup.png")
AR_by_video(2,'my models/best_typeFoot.pt')





