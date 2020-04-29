import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('C:\\Users\\win10\Desktop\\image_processing_exp\\sample images\\parrot.jpg',0)
img=cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('parrot image',img)
cv2.waitKey()
