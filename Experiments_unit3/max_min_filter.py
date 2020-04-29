#max_filter and min_filter
import cv2 
import numpy as np 
  
# Reading the input image 
img = cv2.imread("C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\parrot.jpg",0) 
  
# Taking a matrix of size 5 as the kernel 
kernel = np.ones((5,5), np.uint8) 
   
img_erosion = cv2.erode(img, kernel)   #the filter replaces it with the minimum one
img_dilation = cv2.dilate(img, kernel) #The transformation replaces the central pixel with the maximum value in the running window.
  
cv2.imshow('Input', img) 
cv2.imshow('Erosion', img_erosion) 
cv2.imshow('Dilation', img_dilation) 
  
cv2.waitKey(0)