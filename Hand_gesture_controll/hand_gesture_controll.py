from pyexpat.errors import XML_ERROR_INVALID_TOKEN
from sre_constants import SUCCESS
from turtle import width


import cv2
import os
from matplotlib import image
from cvzone.HandTrackingModule import HandDetector
import numpy as np

width,height=1280,720
image_path="presentation"

sw,sh=int(213*1),int(120*1)
threshold=200
button=False
buttonDely=20
bt_counter=0
annotations=[[]]
annotation_number=0
annotation_start=False

# camera setup
cap=cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

path_image=sorted(os.listdir(image_path))
print(path_image)

image_number=0
detector=HandDetector(detectionCon=0.8,maxHands=1)
while True:
    frame,img=cap.read()
    img=cv2.flip(img,1)
    full_image=os.path.join(image_path,path_image[image_number])
    current_image=cv2.imread(full_image)
    resize_img=cv2.resize(current_image,(1280,720))
    h,w,_=resize_img.shape

    hands,img= detector.findHands(img)
    cv2.line(img,(0,threshold),(width,threshold),(0,255,0),10)

   
    #Adding webcam image on the slider
    #Ass to add this programm need some plugin to controll the situation 
    imgSmall=cv2.resize(img,(sw,sh))
    resize_img[0:sh,w-sw:w]=imgSmall

    
    
    if hands and button==False:
        hand=hands[0]
        fingures=detector.fingersUp(hand)
        cx,cy=hand['center']
        lmlist=hand['lmList']

        xVal=int(np.interp(lmlist[8][0],[300,width//2.2],[0,w]))
        yVal=int(np.interp(lmlist[8][1],[100,height/2],[0,h]))
        index_fingure=xVal,yVal
        # index_fingure=lmlist[8][0],lmlist[8][1]
        # print(fingures)
        print(annotation_number)

        if cy<=threshold:

            if fingures==[1,0,0,0,0]:
                print("left")
                if image_number>0:
                    button=True
                    image_number-=1
                    annotations=[[]]
                    annotation_number=0
                    annotation_start=False

            if fingures==[0,0,0,0,1]:
                print("right")
                if image_number<len(path_image)-1:
                    button=True
                    image_number+=1
                    annotations=[[]]
                    annotation_number=0
                    annotation_start=False

        if fingures==[0,1,1,0,0]:
            cv2.circle(resize_img,index_fingure,12,(255,0,0),cv2.FILLED)     ###

        if fingures==[0,1,0,0,0]:
            if annotation_start is False:
                annotation_start=True
                annotation_number+=1
                annotations.append([])

            cv2.circle(resize_img,index_fingure,12,(255,0,0),cv2.FILLED)
            annotations[annotation_number].append(index_fingure)        
        
        else:
            annotation_start=False

        if fingures==[0,1,1,1,0]:
            if annotation_number>0:
                annotations.pop(-1)
                annotation_number-=1
                button=True

    if button==True:
        bt_counter+=1
    if bt_counter>buttonDely:
        button=False
        bt_counter=0

    for i in range (len(annotations)):
        for j in range (len(annotations[i])):
             if j !=0:
                   cv2.line(resize_img,annotations[i][j-1],annotations[i][j],(255,0,0),12)

    
    cv2.imshow("image",img)
    cv2.imshow("presentation",resize_img)


    key=cv2.waitKey(1)
    if key==ord("q"):
        break