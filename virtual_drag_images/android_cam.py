import cv2
import numpy as np
import urllib.request


# url = "rtsp://172.16.2.45:8080/h264_ulaw.sdp"
url = "rtsp://172.16.2.45:8080/h264_pcm.sdp"
# url = "http://172.16.2.45:8080/onvif/device_service"
cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)



while(True):
    camera, frame = cap.read()
    if frame is not None:
        frame = cv2.resize(frame, (800,800))
        cv2.imshow("Frame", frame)

    cv2.waitKey(1)