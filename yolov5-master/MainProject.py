import cv2
import detection_foot as detect
import foot_size
import shoe_size
# rtsp://192.168.1.101:8080/h264_pcm.sdpi
camera = 3
pathTypefoot = 'my models/best_typeFoot.pt'
pathDetectA4 = 'my models/best_footA4.pt'
detect.detect_by_video(camera,pathTypefoot)
# detect.detect_by_img('D:/GitHub/projectsonteen/Dataset/For train/type foot/images/foot (99).jpg'
#                    ,pathDetectA4)
# detect.detect_by_video(camera,pathDetectA4)

# foot_size.perspectiveA4('input/test1.jpg')
# footSize = foot_size.findSize('output/result_A4.jpg')
# shoe_size.showsize(footSize)




