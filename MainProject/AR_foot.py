import torch
import cv2
import os
import cvzone
from vedo import *
import vedo
from PIL import Image

def overlayImg(pathBack,pathFront,sizeImg,location):
    location = [int(location[0]-sizeImg[0]/2),int(location[1]-sizeImg[1]/2)]
    imgBack = pathBack
    imgFront = cv2.imread(pathFront, cv2.IMREAD_UNCHANGED)
    imgFront = cv2.resize(imgFront,(sizeImg[0],sizeImg[1]))
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
        # results.render()
        testlocation = results.pandas().xyxy[0]
        # print(results.pandas().xyxy[0])
        print(testlocation)
        # print('Xmax',testlocation.xmax[0])
        print(testlocation.empty)
        print('************')


        if testlocation.empty == False :
            # xmin, ymin = testlocation.xmin[0], testlocation.ymin[0]
            # xmax, ymax = testlocation.xmax[0], testlocation.ymax[0]
            # xmin, ymin, xmax, ymax = find_xy_from_class(get_location_to_list(testlocation), 'Top_Foot')
            xmin, ymin, xmax, ymax, anglethumb, caseObj = case3DObj(testlocation)
            if caseObj < 6:
                xmin = int(xmin)
                xmax = int(xmax)
                ymin = int(ymin)
                ymax = int(ymax)
                (x, y) = (xmax + xmin) / 2, (ymax + ymin) / 2
                print('center point : ', x, y)
                frame = cv2.circle(frame, (int(x), int(y)), radius=0, color=(0, 0, 255), thickness=10)
                # if (xmax-xmin)<(ymax-ymin):
                #     sizeImg = int(xmax-xmin)
                # else :
                #     sizeImg = int(ymax-ymin)
                width = int(xmax-xmin)
                long = int(ymax-ymin)
                sizeImg = (width,long)
                location = [int(x), int(y)]
                if caseObj == 1:
                    imgResult = set3Drighttop(frame,sizeImg,location,angle=anglethumb)
                elif caseObj == 2:
                    imgResult = set3Dlefttop(frame,sizeImg,location,angle=anglethumb)
                elif caseObj == 3:
                    imgResult = set3Dleft(frame,sizeImg,location)
                elif caseObj == 4:
                    imgResult = set3Dright(frame,sizeImg,location)
                elif caseObj == 5:
                    imgResult = set3Dstraighttop(frame, sizeImg, location)
                frame = imgResult
                # frame = cv2.circle(imgResult, (int(x), int(y)), radius=0, color=(0, 0, 255), thickness=10)
        key = cv2.waitKey(1)
        if key == ord('c'):
            cv2.destroyAllWindows()
            break
        # results.render()
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
    cropimg('output/shoes.png')
    imgResult = overlayImg(frame, 'output/crop_shoes.png', sizeImg, location)
    set3Dobj(mesh, angle=-angle, way=(1, 0, 0), screenshot=False)
    return imgResult

def set3Dlefttop(frame,sizeImg,location,angle=45):
    set3Dobj(mesh, angle=90,way=(1, 0, 0))
    way=(1, 0, 1)
    set3Dobj(mesh, angle=angle,way=way,screenshot=True)
    cropimg('output/shoes.png')
    imgResult = overlayImg(frame, 'output/crop_shoes.png', sizeImg, location)
    set3Dobj(mesh, angle=-angle, way=way)
    set3Dobj(mesh, angle=-90,way=(1, 0, 0))
    return imgResult

def set3Drighttop(frame,sizeImg,location,angle=45):
    set3Dobj(mesh, angle=90,way=(1, 0, 0))
    way=(-1, 0, -1)
    set3Dobj(mesh, angle=angle,way=way,screenshot=True)
    cropimg('output/shoes.png')
    imgResult = overlayImg(frame, 'output/crop_shoes.png', sizeImg, location)
    set3Dobj(mesh, angle=-angle, way=way)
    set3Dobj(mesh, angle=-90,way=(1, 0, 0))
    return imgResult

def set3Dright(frame,sizeImg,location,angle=270):
    way=(1, 45, 0)
    set3Dobj(mesh, angle=angle,way=way,screenshot=True)
    cropimg('output/shoes.png')
    imgResult = overlayImg(frame, 'output/crop_shoes.png', sizeImg, location)
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


# def get_location_to_list(testlocation):
#     list = []
#     for i in range(len(testlocation.name)) :
#         detail =[]
#         detail.append(testlocation.name[i])
#         detail.append(testlocation.xmin[i])
#         detail.append(testlocation.ymin[i])
#         detail.append(testlocation.xmax[i])
#         detail.append(testlocation.ymax[i])
#         list.append(detail)
#     return list
#
# def find_xy_from_class(list) :
#     index_name = []
#     for i in range(len(list)):
#         if list[i][0] == 'Top_Foot':
#             print('index ',i,' ','Top_Foot')
#             xmin = list[i][1]
#             ymin = list[i][2]
#             xmax = list[i][3]
#             ymax = list[i][4]
#             topfoot = True
#         index_name.append(i)
#
#     print(len(index_name))
#     lenname = len(index_name)
#     if lenname>0 :
#         return xmin, ymin, xmax, ymax
#     else :
#         xmin, ymin, xmax, ymax = 'none','none','none','none'
#         return xmin, ymin, xmax, ymax

def case3DObj(testlocation):
    classname = testlocation.drop_duplicates(subset=['name'])
    listname = []

    classname = classname.reset_index()

    for i in range(len(classname)):
        listname.append(classname.name[i])
    if listname.count('Top_Foot') > 0 and listname.count('Thumb_Foot') > 0:
        topfoot = classname.loc[classname['name'] == 'Top_Foot']
        thumbfoot = classname.loc[classname['name'] == 'Thumb_Foot']
        topfoot = topfoot.reset_index()
        thumbfoot = thumbfoot.reset_index()

        xmin = topfoot.xmin[0]
        ymin = topfoot.ymin[0]
        xmax = topfoot.xmax[0]
        ymax = topfoot.ymax[0]
        sum = (xmax+xmin)/2
        # print(thumbfoot)
        # print(thumbfoot.xmin[1])
        xminthumb = thumbfoot.xmin[0]
        if xminthumb > sum:
            anglethumb = thumbfoot.xmin[0] - sum
            caseObj = 1
            anglethumb = anglethumb / 2
        elif xminthumb < sum:
            anglethumb = sum - thumbfoot.xmin[0]
            caseObj = 2
            anglethumb = anglethumb / 2


    elif listname.count('Left_Foot') > 0:
        leftfoot = classname.loc[classname['name'] == 'Left_Foot']
        leftfoot = leftfoot.reset_index()
        caseObj = 3
        xmin = leftfoot.xmin[0]
        ymin = leftfoot.ymin[0]
        xmax = leftfoot.xmax[0]
        ymax = leftfoot.ymax[0]
        anglethumb = 'none'
    elif listname.count('Right_Foot') > 0:
        rightfoot = classname.loc[classname['name'] == 'Right_Foot']
        rightfoot = rightfoot.reset_index()
        caseObj = 4
        xmin = rightfoot.xmin[0]
        ymin = rightfoot.ymin[0]
        xmax = rightfoot.xmax[0]
        ymax = rightfoot.ymax[0]
        anglethumb = 'none'
    elif listname.count('Top_Foot') > 0:
        topfoot = classname.loc[classname['name'] == 'Top_Foot']
        topfoot = topfoot.reset_index()
        caseObj = 5
        xmin = topfoot.xmin[0]
        ymin = topfoot.ymin[0]
        xmax = topfoot.xmax[0]
        ymax = topfoot.ymax[0]
        anglethumb = 'none'
    else :
        anglethumb = 'none'
        xmin, ymin, xmax, ymax = 'none', 'none', 'none', 'none'
        caseObj = 6
    return xmin, ymin, xmax, ymax, anglethumb, caseObj


# frame = 'input/foot (97).jpg'
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='my models/best_AR.pt')
# results = model(frame)
# results.render()
#
# testlocation = results.pandas().xyxy[0]
# print(testlocation)
# xmin, ymin, xmax, ymax, anglethumb, caseObj = case3DObj(testlocation)
#
#
# print(xmin, ymin, xmax, ymax, anglethumb,caseObj)
# print(listname.count('Tosp_Foot'))

# print(get_location_to_list(testlocation))
# xmin,ymin,xmax,ymax = find_xy_from_class(get_location_to_list(testlocation))
# print(xmin)
# print(ymin)
# print(xmax)
# print(ymax)

mesh = read3DObj("data/AR/supastarOBJ.obj","data/AR/cup.png")
AR_by_video(2,'my models/best_AR.pt')





