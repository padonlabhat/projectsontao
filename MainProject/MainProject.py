import cv2
import detection_foot as detect
import foot_size
import shoe_size
import AR_foot
camera = 2
pathTypefoot = 'my models/best_typeFoot.pt'
pathDetectA4 = 'my models/best_footA4.pt'
#************Test by Img*****************
detect.detect_by_img('input/footA4 (49).jpg',pathDetectA4,crop=True)
# detect.detect_by_img('input/type.jpeg',pathTypefoot,crop=False)
#************Test by Video*****************
# detect.detect_by_video(camera,pathTypefoot)
# detect.detect_by_video(camera,pathDetectA4)
#************Find size*****************
foot_size.perspectiveA4('output/crops.jpg')
footSize = foot_size.findSize('output/1perspectiveA4_result.jpg',140)
shoe_size.showsize(footSize)
#************AR Model*****************
# AR_foot.AR_by_video(camera)

# detect.readAllfile()
