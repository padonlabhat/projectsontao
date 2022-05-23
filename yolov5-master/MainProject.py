import cv2
import detection_foot as detect
import foot_size
import shoe_size
# rtsp://192.168.1.101:8080/h264_pcm.sdpi
camera = 3
detect.detect_by_video(camera,'D:/GitHub/projectsonteen/my models/best_typeFoot.pt')
# detect.detect_by_img('D:/GitHub/projectsonteen/Dataset/For train/type foot/images/foot (99).jpg'
#                    ,'D:/GitHub/projectsonteen/my models/best_typeFoot.pt')
# detect.detect_by_video('rtsp://192.168.1.120:8080/h264_pcm.sdp','D:/GitHub/projectsonteen/my models/best_footA4.pt')

foot_size.perspectiveA4('input/test1.jpg')
footSize = foot_size.findSize('output/result_A4.jpg')
shoe_size.showsize(footSize)

# shoe_size.show()


