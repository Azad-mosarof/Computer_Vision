import math
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np

cap=cv2.VideoCapture(0)

detector=HandDetector(maxHands=2,detectionCon=0.8)
classifier=Classifier('converted_keras/keras_model.h5','converted_keras/labels.txt')
class_name=['A','B','C','D','E','F','G']
offset=20
imgsize=300
folder='data/C'
counter=0

while True:
    _,img=cap.read()
    img=cv2.flip(img,1)
    hands,img=detector.findHands(img,draw=True,flipType=False)
    if hands:
        hand=hands[0]
        x , y , w , h=hand['bbox']
        imgWhite=np.ones((imgsize,imgsize,3),np.uint8)*255
        imgcrop=img[y-offset:y+h+offset,x-offset:x+w+offset]
        shape=imgcrop.shape
        # imgWhite[0:shape[0],0:shape[1]]=imgcrop
        
        aspectratio=h/w
        try:
            if aspectratio>1:
                k=imgsize/h
                cal_w=math.ceil(k*w)
                resizeimage=cv2.resize(imgcrop,(cal_w,imgsize))
                resize_shape=resizeimage.shape
                wgap=math.ceil((imgsize-cal_w)/2)
                imgWhite[0:resize_shape[0],wgap:resize_shape[1]+wgap]=resizeimage
                imgWhite[:,0:wgap]=(200,200,100)
                imgWhite[:,resize_shape[1]+wgap:imgsize]=(200,200,100)
                prediction,index=classifier.getPrediction(imgWhite)
            else:
                k=imgsize/w
                cal_h=math.ceil(k*h)
                resizeimage=cv2.resize(imgcrop,(imgsize,cal_h))
                resize_shape=resizeimage.shape
                hgap=math.ceil((imgsize-cal_h)/2)
                imgWhite[hgap:resize_shape[0]+hgap,0:resize_shape[1]]=resizeimage
                imgWhite[0:hgap,:]=(200,200,100)
                imgWhite[resize_shape[0]+hgap:imgsize,:]=(200,200,100)
                prediction,index=classifier.getPrediction(imgWhite)
            cv2.imshow("White_image",imgWhite)
            cv2.imshow("Croped_Hand",imgcrop)
        except:
            shape=img.shape
            cx,cy=int(shape[0]/2),int(shape[1]/2)
            img=cv2.putText(img,"Please bring your hand inside the boundary",(0,cx),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),2)

    cv2.imshow("Data_collection",img)
  
    k = cv2.waitKey(1) & 0xFF