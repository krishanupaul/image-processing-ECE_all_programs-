import cv2
import numpy as np

img=cv2.imread('C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\parrot.jpg')
img = cv2.resize(img, (750, 750))
imagem = cv2.bitwise_not(img)
cv2.imshow('image',img)
cv2.imshow('negative_image',imagem)
cv2.waitKey(0) #mandatory whenever using imshow
cv2.destroyAllWindows()