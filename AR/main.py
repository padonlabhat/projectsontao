from vedo import *
import vedo
# mesh = Mesh("data/10055_Gray_Wolf_v1_L3.obj",)
# mesh.texture("data/10055_Gray_Wolf_Diffuse_v1.jpg", scale=0.1)
# mesh = Mesh("data/supastarOBJ.obj",)
# mesh.texture("data/10055_Gray_Wolf_Diffuse_v1.jpg", scale=0.1)
# mesh.print()
# mesh.rotate(90, axis=(1,0,0), point=(0, 0, 0), rad=False)
# mesh.show()

# import cvzone
# import cv2
# imgBack = cv2.imread("data/background.jpg")
# imgFront = cv2.imread("data/Screenshot (7).png", cv2.IMREAD_UNCHANGED)
# imgFront = cv2.resize(imgFront,(500,500))
# imgResult = cvzone.overlayPNG(imgBack, imgFront, [100,100])
def read3DObj(pathObj,pathDesign,angle,way):
    mesh = Mesh(pathObj)
    mesh.texture(pathDesign, scale=1)
    # settings.screenshotTransparentBackground = True
    # mesh.print()
    mesh.rotate(angle, axis=way, point=(0, 0, 0), rad=False)
    # mesh.show()
    plotter = vedo.Plotter(offscreen=True)
    plotter += mesh
    plotter.show().screenshot('shoes.png')
read3DObj("data/supastarOBJ.obj","data/10055_Gray_Wolf_Diffuse_v1.jpg",angle=90,way=(1, 0, 0))