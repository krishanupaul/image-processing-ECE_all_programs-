import cv2

A=cv2.imread('C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\1.jpg')
B=cv2.imread('C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\4.jpg')

for x in range(750):
        for y in range(750):
            A[x,y]=B[x,y]-A[x,y]
            
cv2.imshow('image',A)
cv2.waitKey(0)            