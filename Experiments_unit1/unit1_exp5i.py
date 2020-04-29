import cv2
import numpy as np
import matplotlib.pyplot as plt
a=127
img=cv2.imread('C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\parrot.jpg',0)
cv2.imshow('image',img)
cv2.waitKey()
for x in range(256):
  for y in range(384):
      if img[x,y]>a:
          img[x,y]
      else:
          img[x,y]=0
cv2.imshow('image',img)
cv2.waitKey()