import cv2
import numpy as np

img=cv2.imread('C:\\Users\\win10\Desktop\\image_processing_exp\\sample images\\apple.jpg',0)

#nearest neighbour interpolation
near_img = cv2.resize(img,None, fx = 10, fy = 10, interpolation = cv2.INTER_NEAREST)

#bilinear interpolation
bilinear_img = cv2.resize(img,None, fx = 10, fy = 10, interpolation = cv2.INTER_LINEAR)


cv2.imshow('image',near_img)
cv2.waitKey()

cv2.imshow('image',bilinear_img)
cv2.waitKey()