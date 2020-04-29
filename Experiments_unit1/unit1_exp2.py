import cv2
import numpy as np

img = cv2.imread('C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\parrot.jpg')

for x in range(256):
    for y in range(384):
        print(img[x, y])
