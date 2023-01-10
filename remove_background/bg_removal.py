import os
from tkinter import Frame
import cv2
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt
import urllib

#store background image in a list
img_path = "images"
bg_images = os.listdir(img_path)

image_index = 4
# bg_image = cv2.imread(img_path+'/'+bg_images[image_index])
# bg_image = cv2.cvtColor(bg_image, cv2.COLOR_BGR2RGB)

def url_to_image(url):
	resp = urllib.request.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)

	# return the image
	return image

bg_image = url_to_image("data:image/jpeg;base64,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")
bg_image = cv2.cvtColor(bg_image, cv2.COLOR_BGR2RGB)

#initialize mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation
selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

img = cv2.imread("/home/azadm/Downloads/WhatsApp Image 2022-04-11 at 12.43.42 PM.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
h, w, c = img.shape

result = selfie_segmentation.process(img)
mask = result.segmentation_mask

condition = np.stack(
    (result.segmentation_mask,) * 3, axis=-1
) > 0.5

bg_image = cv2.resize(bg_image, (w, h))
output_img = np.where(condition, img, bg_image)
plt.imshow(output_img)
plt.show()
plt.imsave("converted.png",output_img)

#Read frames from a webcam
cap = cv2.VideoCapture(0)
while cap.isOpened:
    _, img = cap.read()
    img = cv2.flip(img,1)
    h, w, c = img.shape
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    result = selfie_segmentation.process(img)
    mask = result.segmentation_mask
    cv2.imshow('mask',mask)

    #Replace the background with an image
    condition = np.stack(
        (result.segmentation_mask,) * 3, axis=-1
    ) > 0.5

    #resize the background image to the same image as original image
    bg_image = cv2.resize(bg_image, (w, h))

    #combine frame and background image to the same size of the original image
    output_img = np.where(condition, img, bg_image)
    cv2.imshow("output_image", output_img)

    cv2.imshow("image",img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('d'):
        if image_index != len(bg_images) - 1:
            image_index += 1
        else:
            image_index = 0
    bg_image = cv2.imread(img_path+'/'+bg_images[image_index])