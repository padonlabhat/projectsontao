import cv2
import numpy as np
#
# image = cv2.imread("data/footA4.jpg")
#
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# image_1 = cv2.imread("data/footA4.jpg")
# # print(image_1)
#
# image_1[50: 100, 50:100] = [255, 0, 0]
#
# image_2 = cv2.imread("data/qr.png")
# resized_image_2 = cv2.resize(image_2, dsize=(100, 100))
#
# image_1[50:150, 50:150] = resized_image_2
#
# image_3 = cv2.imread("data/qr.png", cv2.IMREAD_UNCHANGED)
#
# ones = np.ones((image_1.shape[0], image_1.shape[1]))*255
# image_1 = np.dstack([image_1, ones])
#
# image_1[150:250, 150:250] = image_3
#
#
# cv2.imshow('ul',image_1)
#
# cv2.waitKey(0)

# import cv2
# import numpy as np
#
# img1 = cv2.imread("data/footA4.jpg")
# img2 = cv2.imread("data/qr.png")
# # Img2 = cv2.resize (img2, (480331)) # unified picture size
#
# dst = cv2.addWeighted(img1,0.5,img2,0.5,0)
#
# cv2.imshow('dst',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

def logoOverlay(image,logo,alpha=1.0,x=0, y=0, scale=1.0):
    (h, w) = image.shape[:2]
    image = np.dstack([image, np.ones((h, w), dtype="uint8") * 255])

    overlay = cv2.resize(logo, None,fx=scale,fy=scale)
    (wH, wW) = overlay.shape[:2]
    output = image.copy()
    # blend the two images together using transparent overlays
    try:
        if x<0 : x = w+x
        if y<0 : y = h+y
        if x+wW > w: wW = w-x
        if y+wH > h: wH = h-y
        print(x,y,wW,wH)
        overlay=cv2.addWeighted(output[y:y+wH, x:x+wW],alpha,overlay[:wH,:wW],1.0,0)
        output[y:y+wH, x:x+wW ] = overlay
    except Exception as e:
        print("Error: Logo position is overshooting image!")
        print(e)

    output= output[:,:,:3]
    return output


background = cv2.imread('image.jpeg')
overlay = cv2.imread('logo.png', cv2.IMREAD_UNCHANGED)

# print(overlay.shape) # must be (x,y,4)
# print(background.shape) # must be (x,y,3)

# downscale logo by half and position on bottom right reference
out = logoOverlay(background,overlay,scale=0.5,y=-100,x=-100)

cv2.imshow("test",out)
cv2.waitKey(0)