import cv2
import numpy as np
import math

maxValue = 255
img=cv2.imread("C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\wb.jpg",0)
img = cv2.resize(img, (750, 750))
cv2.imshow('fft_image',img)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
fft_image=np.abs(fshift)

C = 255 / math.log(1 + maxValue,10)
dimensions = img.shape
rows = img.shape[0]
columns = img.shape[1]
for i in range(rows):
    for j in range(columns):
        img[i][j]=round(C*math.log(fft_image[i][j]+1),10)

cv2.imshow('image',img)
#cv2.imshow('fft_image',fft_image)
cv2.waitKey(0)
cv2.destroyAllWindows()