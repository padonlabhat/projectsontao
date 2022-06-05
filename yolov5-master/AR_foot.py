import torch
import cv2
import os
import cvzone
def overlayImg(pathBack,pathFront,sizeImg,location):
    location = [int(location[0]-sizeImg/2),int(location[1]-sizeImg/2)]
    imgBack = cv2.imread(pathBack)
    imgFront = cv2.imread(pathFront, cv2.IMREAD_UNCHANGED)
    imgFront = cv2.resize(imgFront,(sizeImg,sizeImg))
    imgResult = cvzone.overlayPNG(imgBack, imgFront, location)
    return imgResult



def AR_foot(pathImg, pathModel):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=pathModel)
    frame = pathImg
    results = model(frame)
    # results.imgs  # array of original images (as np array) passed to model for inference
    # results.render()  # updates results.imgs with boxes and labels
    # crops = results.crop(save=True)  # cropped detections dictionary
    # cv2.imshow("Image",crops)
    # cv2.waitKey(0)
    testlocation = results.pandas().xyxy[0]
    print(results.pandas().xyxy[0])
    print(testlocation)
    print(testlocation.xmax[0])
    x1, y1 = testlocation.xmin[0], testlocation.ymin[0]
    x2, y2 = testlocation.xmax[0], testlocation.ymax[0]
    (x, y) = (x2 + x1) / 2, (y2 + y1) / 2
    print(x, y)

    image_rgb = cv2.cvtColor(results.imgs[0], cv2.COLOR_BGR2RGB)
    image_rgb = cv2.circle(image_rgb, (int(x), int(y)), radius=0, color=(0, 0, 255), thickness=10)
    cv2.imshow('img', image_rgb)
    cv2.waitKey(0)

    return x1,y1,x2,y2,x,y

# img = overlayImg()
location = AR_foot('D:/GitHub/projectsonteen/Dataset/For train/type foot/images/foot (99).jpg','my models/best_typeFoot.pt')
print(location)

imgResult = overlayImg('D:/GitHub/projectsonteen/Dataset/For train/type foot/images/foot (99).jpg'
           ,'D:/GitHub/projectsonteen/AR/m1.png'
           ,int(location[3]-location[1])
           ,[int(location[4]),int(location[5])])
cv2.imshow("Image", imgResult)
cv2.waitKey(0)