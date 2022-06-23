import cv2
import detection_foot as detect
import foot_size
import shoe_size
import AR_foot
camera = 1
pathTypefoot = 'my models/best_typeFoot.pt'
pathDetectA4 = 'my models/best_footA4.pt'
# detect.detect_by_video(camera,pathTypefoot)
# detect.detect_by_img('D:/GitHub/projectsonteen/Dataset/For train/type foot/images/foot (99).jpg'
#                    ,pathTypefoot)


# detect.detect_by_video(camera,pathDetectA4)
# foot_size.perspectiveA4('output/crops.jpg')
# footSize = foot_size.findSize('output/1perspectiveA4_result.jpg',127)
# shoe_size.showsize(footSize)

AR_foot.AR_by_video(2)


