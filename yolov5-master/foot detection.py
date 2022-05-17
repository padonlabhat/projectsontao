import torch
import cv2


def take_a_photo():
    cap = cv2.VideoCapture(1)
    # cap = cv2.VideoCapture('rtsp://192.168.1.101:8080/h264_pcm.sdp')
    while True:
        _, frame = cap.read()

        # frame = cv2.resize(frame, (800, 800))
        results = model(frame)
        results.render()
        # results.save()
        # print(results.pandas().xyxy[0])
        image_rgb = cv2.cvtColor(results.imgs[0], cv2.COLOR_BGR2RGB)
        cv2.imshow('preview-frame',frame)
        key = cv2.waitKey(1)

        if key == ord('c'):
        #     # _, frame = cap.read()
        #     # frame = cv2.resize(frame, (800, 800))
        #     cropped_image = frame[150:650, 100:700]
        #     cv2.imwrite('capture.jpg',cropped_image)

            cv2.destroyAllWindows()
            break

def detect_from_img():
    frame = 'D:/GitHub/projectsonteen/yolov5-master/test/foot (37).jpg'
    results = model(frame)
    results.render()
    print(results.pandas().xyxy[0])
    #
    image_rgb = cv2.cvtColor(results.imgs[0], cv2.COLOR_BGR2RGB)
    cv2.imshow('img', image_rgb)
    cv2.waitKey(0)

model = torch.hub.load('ultralytics/yolov5', 'custom', path='D:/GitHub/projectsonteen/yolov5-master/my models/best.pt')
take_a_photo()
# detect_from_img()

