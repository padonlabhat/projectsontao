import detection_foot as detect
import sizefoot
# rtsp://192.168.1.101:8080/h264_pcm.sdp
# detect.detect_by_video(1,'D:/GitHub/projectsonteen/my models/best_typeFoot.pt')
# detect.detect_by_img('D:/GitHub/projectsonteen/Dataset/For train/type foot/images/foot (99).jpg'
#                    ,'D:/GitHub/projectsonteen/my models/best_typeFoot.pt')
# detect.detect_by_video('rtsp://192.168.1.120:8080/h264_pcm.sdp','D:/GitHub/projectsonteen/my models/best_footA4.pt')
#
# sizefoot.perspectiveA4('output/crops.jpg')
sizefoot.findSize('output/result_A4.jpg')
