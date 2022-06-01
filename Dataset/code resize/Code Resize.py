import os
import cv2

path = 'C:/Users/USER/Desktop/projectsontao/Dataset/imgFootAR/TopFoot/'
dir = os.listdir(path)
# print(path)
# print(len(dir))
# print(dir)

for i in dir:
    print(path + i)
    img = cv2.imread(path + i)
    print(img)
    img = cv2.resize(img,(500,500))
    cv2.imwrite("C:/Users/USER/Desktop/projectsontao/Dataset/For train/TopFoot/images/"+i,img)

# cv2.imshow('image',img)
# cv2.waitKey(0)

