from cgitb import grey
from cv2 import IMREAD_COLOR
import numpy as np
import time
import os
from matplotlib import image, pyplot as plt
import cv2
x0=200
y0=100
l=100
s=l*(np.sin(np.pi/30)/np.sin(np.pi*87/180))
print(s)
x1=x0
y1=200
print(x1,y1)
n=0
image=cv2.imread("bg_img.jpg",IMREAD_COLOR)
cv2.imshow("image",image) 
for n in range(60):
    

    x1=x1+(s*np.cos(n*(np.pi/30)))
    y1=y1-(s*np.sin(n*(np.pi/30)))
    print(x1,y1)
    cv2.line(image,(x0,y0),(x1,y1),(0,0,255),5)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    time.sleep(1)


  






   