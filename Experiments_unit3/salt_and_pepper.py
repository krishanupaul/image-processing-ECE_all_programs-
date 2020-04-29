import numpy as np
import random
import cv2

def sp_noise(image, prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()    #Generates a random float number between 0.0 to 1.0
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

image = cv2.imread("C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\parrot.jpg",0) # Only for grayscale image
noise_img = sp_noise(image,0.05)
cv2.imshow('salt and pepper',noise_img)
cv2.imwrite('C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\avg_parrot.jpg',noise_img)
cv2.waitKey(0)