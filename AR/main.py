from vedo import *
# mesh = Mesh("data/10055_Gray_Wolf_v1_L3.obj",)
# mesh.texture("data/10055_Gray_Wolf_Diffuse_v1.jpg", scale=0.1)
mesh = Mesh("data/supastarOBJ.obj",)
mesh.texture("data/10055_Gray_Wolf_Diffuse_v1.jpg", scale=0.1)
mesh.print()
mesh.show()

# import cvzone
# import cv2
# imgBack = cv2.imread("data/background.jpg")
# imgFront = cv2.imread("data/Screenshot (7).png", cv2.IMREAD_UNCHANGED)
# imgFront = cv2.resize(imgFront,(500,500))
# imgResult = cvzone.overlayPNG(imgBack, imgFront, [100,100])
