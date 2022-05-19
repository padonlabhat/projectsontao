# cm = float(input("centimeter : "))

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

# adidas(cm)
# nike(cm)