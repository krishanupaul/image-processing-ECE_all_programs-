import cv2
import math
import numpy as np

maxValue=255
img=cv2.imread("C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\parrot.jpg",0)
img = cv2.resize(img, (750, 750))
C = 255 / math.log(1 + maxValue,10)
cv2.imshow('original',img)
dimensions = img.shape
rows = img.shape[0]
columns = img.shape[1]
for i in range(rows):
    for j in range(columns):
        img[i][j]=round(C*math.log(img[i][j]+1),10)
cv2.imshow('log',img)
cv2.waitKey(0)
cv2.destroyAllWindows()