import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\win10\\Desktop\\image_processing_exp\\sample images\\wb.jpg", 0)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)
phase_spectrum = np.angle(dft_shift)

ax1 = plt.subplot(1, 2, 1)
ax1.imshow(img, cmap='gray')

ax2 = plt.subplot(1, 2, 2)
ax2.imshow(phase_spectrum, cmap='gray')

plt.show()