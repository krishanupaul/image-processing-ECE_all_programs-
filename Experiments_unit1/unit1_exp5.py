"spatial and grey level resolution"

import cv2

img=cv2.imread('C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\parrot.jpg',0)
img1=cv2.imread('C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\parrot.jpg',0)
for x in range(256):
        for y in range(384):
            img[x,y]=img[x,y]%32
            #img[x,y]=img[x,y]*32
        
            
cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.imshow('changing grey level image',img1)
cv2.waitKey(0)