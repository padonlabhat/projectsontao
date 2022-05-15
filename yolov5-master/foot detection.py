import torch
import cv2


# # Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model = torch.hub.load('ultralytics/yolov5', 'custom', path='D:/GitHub/projectsonteen/yolov5-master/my models/best.pt/')
# model = torch.hub.load('path/to/yolov5', 'custom', path='path/to/best.pt', source='local')
# Image
im = 'D:/GitHub/projectsonteen/yolov5-master/test/foot (37).jpg/'

# Inference
results = model(im)

results.pandas().xyxy[0]
# crops = results.crop(save=True)