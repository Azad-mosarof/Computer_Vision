import cv2
import numpy as np
import mediapipe as mp
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

plotY = LivePlot(640, 480, [10, 40])
plotLip = LivePlot(640, 480, [1,60])

idList = [22, 23, 24, 25, 26, 110, 157, 158, 159, 160, 161, 246, 173]

# lipsUpperOuter = [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291]
lipsUpperOuter = [185, 40, 39, 37, 0, 267, 269, 270, 409, 291]
lipsLowerOuter = [146, 91, 181, 84, 17, 314, 405, 321, 375, 291]
lipsUpperInner = [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308]
lipsLowerInner = [78, 95, 88, 178, 87, 14, 317, 402, 318, 324, 308]

outer_lipId = [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291]
inner_lipID = [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308, 78, 95, 88, 178, 87, 14, 317, 402, 318, 324, 308]

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (800, 500))

    img, faces = detector.findFaceMesh(img, draw=False)
    
    if faces:
        face = faces[0]
        for id in idList:
            cv2.circle(img, face[id], 2, (255, 0, 255), cv2.FILLED)
        
        for id in inner_lipID:
            cv2.circle(img, face[id], 2, (255, 0, 255), cv2.FILLED)

        leftUp = face[159]
        leftDown = face[23]
        leftLeft = face[130]
        leftRight = face[243]

        len_hor, _ = detector.findDistance(leftLeft, leftRight)
        len_ver, _ = detector.findDistance(leftUp, leftDown) 

        cv2.line(img, leftLeft, leftRight, (0, 200, 0), 2) 
        cv2.line(img, leftUp, leftDown, (0, 200, 0), 2)

        ratio = (len_ver/len_hor)*100

        lipLeft = face[61]
        lipRight = face[291]

        def lip_tracking():
            sum = 0
            for i in range(0, len(lipsUpperOuter)-1):
                lipUpper = face[lipsUpperOuter[i]]
                lipBelow = face[lipsLowerOuter[i]]

                lip_len_hor, _ = detector.findDistance(lipLeft, lipRight)
                lip_len_ver, _ = detector.findDistance(lipUpper, lipBelow)

                cv2.line(img, lipLeft, lipRight, (0, 200, 0), 2) 
                cv2.line(img, lipUpper, lipBelow, (0, 200, 0), 2)
        
                if lip_len_ver:
                    lip_ratio = (lip_len_ver / lip_len_hor) * 100
                    sum += lip_ratio
            
            if sum:
                avg_lip_ratio = sum / (len(lipsUpperOuter)-1)
                lip_plot = plotLip.update(avg_lip_ratio)
                cv2.imshow(f"Lip_signal_Plot", lip_plot)

        lip_tracking()
        
        img_plot = plotY.update(ratio)
        cv2.imshow("Image_plot",img_plot)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord('q'):
        break