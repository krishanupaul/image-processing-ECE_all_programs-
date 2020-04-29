import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('C:\\Users\\win10\Desktop\\image_processing_exp\\sample images\\parrot.jpg',0)
cv2.imshow('parrot image',img)
cv2.waitKey()
