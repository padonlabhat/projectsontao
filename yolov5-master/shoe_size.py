# cm = float(input("centimeter : "))
import cv2
import matplotlib.pyplot as plt
def nike(cm):
    nikeM = "-"
    nikeWM = "-"
    if (cm >= 22) and (cm < 22.25):
        nikeM = "-"
        nikeWM = "5"
    elif (cm >= 22.25) and (cm < 22.75):
        nikeM = "-"
        nikeWM = "5.5"
    elif (cm >= 22.75) and (cm < 23.25):
        nikeM = "-"
        nikeWM = "6"
    elif (cm >= 23.25) and (cm < 23.75):
        nikeM = "-"
        nikeWM = "6.5"
    elif (cm >= 23.75) and (cm < 24.5):
        nikeM = "-"
        nikeWM = "7"
    elif (cm >= 24.5) and (cm < 25):
        nikeM = "-"
        nikeWM = "8"
    elif (cm >= 25) and (cm < 25.25):
        nikeM = "7"
        nikeWM = "8"
    elif (cm >= 25.25) and (cm < 25.5):
        nikeM = "7"
        nikeWM = "8.5"
    elif (cm >= 25.5) and (cm < 26):
        nikeM = "8"
        nikeWM = "8.5"
    elif (cm >= 26) and (cm < 26.5):
        nikeM = "8.5"
        nikeWM = "9.5"
    elif (cm >= 26.5) and (cm <= 27):
        nikeM = "9"
        nikeWM = "10"
    elif (cm > 27) and (cm < 27.5):
        nikeM = "9.5"
        nikeWM = "-"
    elif (cm >= 27.5) and (cm < 28.5):
        nikeM = "10"
        nikeWM = "-"
    elif (cm >= 28.5) and (cm < 29.5):
        nikeM = "11"
        nikeWM = "-"
    elif (cm >= 29.5) and (cm < 30.5):
        nikeM = "12"
        nikeWM = "-"
    elif (cm >= 30.5) and (cm <= 31):
        nikeM = "13"
        nikeWM = "-"

    print("Nike Men US : ",nikeM,"\nNike Women US : ",nikeWM)
    return nikeM,nikeWM
def adidas(cm):
    adidasM = "-"
    adidasWM = "-"
    if (cm >= 22) and (cm < 22.3):
        adidasM = "4"
        adidasWM = "5"
    elif (cm >= 22.3) and (cm < 22.7):
        adidasM = "4.5"
        adidasWM = "5.5"
    elif (cm >= 22.7) and (cm < 23.1):
        adidasM = "5"
        adidasWM = "6"
    elif (cm >= 23.1) and (cm < 23.55):
        adidasM = "5.5"
        adidasWM = "6.5"
    elif (cm >= 23.55) and (cm < 24):
        adidasM = "6"
        adidasWM = "7"
    elif (cm >= 24) and (cm < 24.4):
        adidasM = "6.5"
        adidasWM = "7.5"
    elif (cm >= 24.4) and (cm < 24.8):
        adidasM = "7"
        adidasWM = "8"
    elif (cm >= 24.8) and (cm < 25.25):
        adidasM = "7.5"
        adidasWM = "8.5"
    elif (cm >= 25.25) and (cm < 25.7):
        adidasM = "8"
        adidasWM = "9"
    elif (cm >= 25.7) and (cm < 26.1):
        adidasM = "8.5"
        adidasWM = "9.5"
    elif (cm >= 26.1) and (cm < 26.5):
        adidasM = "9"
        adidasWM = "10"
    elif (cm >= 26.5) and (cm < 26.9):
        adidasM = "9.5"
        adidasWM = "10.5"
    elif (cm >= 26.9) and (cm < 27.35):
        adidasM = "10"
        adidasWM = "11"
    elif (cm >= 25.35) and (cm < 27.8):
        adidasM = "10.5"
        adidasWM = "11.5"
    elif (cm >= 27.8) and (cm < 28.2):
        adidasM = "11"
        adidasWM = "12"
    elif (cm >= 28.2) and (cm < 28.6):
        adidasM = "11.5"
        adidasWM = "12.5"
    elif (cm >= 28.6) and (cm < 29.05):
        adidasM = "12"
        adidasWM = "13"
    elif (cm >= 29.05) and (cm < 29.5):
        adidasM = "12.5"
        adidasWM = "13.5"
    elif (cm >= 29.5) and (cm < 29.9):
        adidasM = "13"
        adidasWM = "14"
    elif (cm >= 29.9) and (cm < 30.3):
        adidasM = "13.5"
        adidasWM = "14.5"
    elif (cm >= 30.3) and (cm < 30.7):
        adidasM = "14"
        adidasWM = "15"
    elif (cm >= 30.7) and (cm <= 31):
        adidasM = "14.5"
        adidasWM = "15.5"

    print("Adidas Men US : ",adidasM,"\nAdidas Women US : ",adidasWM)
    return adidasM,adidasWM

def showsize(footSize):
    length, width = footSize
    nikeM,nikeWM = nike(length)
    adidasM, adidasWM = adidas(length)
    img = cv2.imread('output/findsize_7ALLBOX.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    colortext = (0,0,255)
    cv2.putText(img=img, text="length : "+str(length)+' CM', org=(150, 250), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=5,
                color=colortext, thickness=3)
    cv2.putText(img=img, text="width : "+str(width)+' CM', org=(150, 450), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=5,
                color= colortext , thickness=3)
    cv2.putText(img=img, text="nikeMen US : "+str(nikeM), org=(150, 650), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=5,
                color= colortext , thickness=3)
    cv2.putText(img=img, text="nikeWomen US : "+str(nikeWM), org=(150, 850), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=5,
                color= colortext , thickness=3)
    cv2.putText(img=img, text="adidasMen US : "+str(adidasM), org=(150, 1050), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=5,
                color= colortext , thickness=3)
    cv2.putText(img=img, text="adidasWomen US : "+str(adidasWM), org=(150, 1250), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=5,
                color= colortext , thickness=3)


    plt.imshow(img)
    plt.show()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.imwrite('output/result_ALL_size.jpg', img)
