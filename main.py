from skimage import io
import numpy as np
import dithering as dt
import matplotlib.pyplot as plt

Img = io.imread("lena512color.tiff")
Dithered = dt.dither_image(Img)

fig = plt.figure("RGB Dithering")
 
ax = fig.add_subplot(1, 2, 1)
plt.imshow(Img)
plt.axis("off")
 
ax = fig.add_subplot(1, 2, 2)
plt.imshow(Dithered)
plt.axis("off")


plt.show()
        