import cv2
import numpy as np
img=cv2.imread("C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\parrot.jpg",0)
cv2.imshow('original',img)
dimensions = img.shape
rows = img.shape[0]
columns = img.shape[1]
for i in range(rows):
    for j in range(columns):
        img[i][j]=img[i][j]&32
cv2.imshow('bit_plane_slicing',img)
cv2.waitKey(0) #mandatory whenever using imshow
cv2.destroyAllWindows()
        
