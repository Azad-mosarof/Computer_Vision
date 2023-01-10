import cv2
import numpy as np
import cvzone as cv
from cvzone.HandTrackingModule import HandDetector
import os


cap = cv2.VideoCapture(0)
cap.set(3, 1600)
cap.set(4, 1600)

detector = HandDetector(detectionCon=0.7)

class DragImg():

    def __init__(self,path,posOrigin,ImgType):

        self.posOrigin = posOrigin
        self.path = path
        self.imgType = ImgType

        if self.imgType == 'png':
            self.img = cv2.imread(self.path, cv2.IMREAD_UNCHANGED)
        else:
            self.img = cv2.imread(self.path)
        
        self.size = self.img.shape[:2]
    
    def update(self,cursor):
        ox, oy = self.posOrigin
        h, w = self.size
        if ox <cursor[0]< ox+w and oy <cursor[1]< oy+h:
            self.posOrigin = cursor[0] - w//2, cursor[1] - h//2


img1 = cv2.imread("/home/azadm/vs-code-files/opencv/virtual_drag_images/image/ImagesJPG/1.jpg")
img2 = cv2.imread("/home/azadm/vs-code-files/opencv/virtual_drag_images/image/ImagesPNG/1.png",cv2.IMREAD_UNCHANGED)
# ox, oy = 200, 200

path = "/home/azadm/vs-code-files/opencv/virtual_drag_images/image/ImagesPNG"
myLIst = os.listdir(path)
print(myLIst)

listing = []
for x,pathImg in enumerate(myLIst):
    if 'png' in pathImg:
        imgType = 'png'
    else:
        imgType = 'jpg'

    listing.append(DragImg(f'{path}/{pathImg}',[50+x*100,50],imgType))

print(len(listing))

while True:
    _, img = cap.read()
    img = cv2.flip(img,1)
    hands, img = detector.findHands(img,flipType=False)

    try:
        for imgObj in listing:
            h, w, _ = imgObj.img.shape
            ox, oy =imgObj.posOrigin
            if imgObj.imgType == 'png':
                img = cv.overlayPNG(img, imgObj.img, [ox,oy])
            else:
                img[oy:oy+h,ox:ox+w] = imgObj.img
    except:
        pass

    if hands:
        lmList = hands[0]['lmList']
        length, info, img = detector.findDistance(lmList[8][:-1],lmList[12][:-1],img)
        if length < 26 :
            cursor = lmList[8]
            for imgObj in listing:
                imgObj.update(cursor)

    cv2.imshow("image",img)
    cv2.waitKey(1)

