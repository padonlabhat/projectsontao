from vedo import *
mesh = Mesh("data/10055_Gray_Wolf_v1_L3.obj",)
mesh.texture("data/10055_Gray_Wolf_Diffuse_v1.jpg", scale=0.1)
mesh.print()
mesh.show()