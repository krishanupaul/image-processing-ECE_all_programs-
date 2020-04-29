import cv2
import numpy as np
import math


# Power law transformation
img = cv2.imread("C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\parrot.jpg",0)  
cv2.imshow('Original_Image',img)
c=255/(math.pow(255,4))
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i][j] = c*math.pow(img[i][j],4)

cv2.imshow('Modified_Image',img)
cv2.waitKey(0)