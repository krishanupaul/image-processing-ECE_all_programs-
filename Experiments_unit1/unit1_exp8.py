import numpy as np
import PIL
import math
import cv2

# Load image and ensure RGB - just in case palettised
im=cv2.imread("C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\distance_image.png")

# Make numpy array from image
npimage=np.array(im)

# Describe what a single red pixel looks like
red=np.array([255,0,0],dtype=np.uint8)

# Find [x,y] coordinates of all red pixels
reds=np.where(np.all((npimage==red),axis=-1))

# Describe what a single blue pixel looks like
blue=np.array([0,0,255],dtype=np.uint8)

# Find [x,y] coordinates of all blue pixels
blues=np.where(np.all((npimage==blue),axis=-1))

dx2 = (blues[0][0]-reds[0][0])**2          # (200-10)^2
dy2 = (blues[1][0]-reds[1][0])**2          # (300-20)^2
distance = math.sqrt(dx2 + dy2)

print(distance)