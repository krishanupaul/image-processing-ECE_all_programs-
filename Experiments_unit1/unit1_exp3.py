import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('B:\\wall\\1.jpg',0)
cv2.imshow('image',img)
cv2.waitKey()
dim = (400, 600)
resized = cv2.resize(img, dim)
for x in range(100):
  for y in range(200):
      resized[x,y]=0

cv2.imshow('image',resized)
cv2.waitKey()