import cv2
import numpy as np
from mss import mss
import keyboard
import pyautogui
def Gettrackpos():
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")
    l = np.array([l_h, l_s, l_v])
    u = np.array([u_h, u_s, u_v])
    return l,u
def nothing(X):
    pass

def GetLowerUpperValue(img):
    while True:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        switch=cv2.getTrackbarPos("Print", "Tracking")
        if switch==0:
            l,u=Gettrackpos()
            mask=cv2.inRange(hsv,l,u)
            res=cv2.bitwise_and(img,img,mask=mask)
            cv2.imshow("image",res)
            cv2.waitKey(1)
        else:
            print("Lower: ",l)
            print("Upper: ",u)
            cv2.destroyAllWindows()
            break
print("keep mouse cursor on required pixel area and press s")
while True:
    x,y=pyautogui.position()
    #x,y=10,20
    coordinates = {
        'top': y,
        'left': x,
        'width': 400,
        'height': 400,
    }
    if keyboard.is_pressed("s"):
        cv2.namedWindow("Tracking")
        cv2.resizeWindow("Tracking", 400, 350)
        cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
        cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
        cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
        cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
        cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
        cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)
        cv2.createTrackbar("Print", "Tracking", 0, 1, nothing)
        img = np.array(mss().grab(coordinates))
        GetLowerUpperValue(img)
        break

