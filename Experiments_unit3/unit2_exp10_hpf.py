import cv2
import numpy as np

img = cv2.imread("C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\parrot.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

#sobel
kernel_x = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
kernel_y = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
img_sobelx = cv2.filter2D(gray, -1, kernel_x)
img_sobely = cv2.filter2D(gray, -1, kernel_y)
img_sobel = img_sobelx + img_sobely


#prewitt
kernelx = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
kernely = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
img_prewittx = cv2.filter2D(gray, -1, kernelx)
img_prewitty = cv2.filter2D(gray, -1, kernely)


cv2.imshow("Original Image", img)
cv2.imshow("Sobel X", img_sobelx)
cv2.imshow("Sobel Y", img_sobely)
cv2.imshow("Sobel", img_sobel)
cv2.imshow("Prewitt X", img_prewittx)
cv2.imshow("Prewitt Y", img_prewitty)
cv2.imshow("Prewitt", img_prewittx + img_prewitty)


cv2.waitKey(0)
cv2.destroyAllWindows()