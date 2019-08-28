import numpy as np

def share_error(Dithered, quant_error, x, y):
        Xmax = Dithered.shape[0]
        Ymax = Dithered.shape[1]
        if(x + 1 < Xmax):
                Dithered[x + 1, y    ] = Dithered[x + 1, y    ] + (quant_error * 7 / 16)
        
        if(x - 1 > 0 and (y + 1 <Ymax)):
                Dithered[x - 1, y + 1] = Dithered[x - 1, y + 1] + (quant_error * 3 / 16)
        
        if(y + 1 < Ymax):
                Dithered[x    , y + 1] = Dithered[x    , y + 1] + (quant_error * 5 / 16)
        
        if((x + 1 < Xmax) and (y + 1 <Ymax)):
                Dithered[x + 1, y + 1] = Dithered[x + 1, y + 1] + (quant_error * 1 / 16)


def dither_image(Img):
        Shape = Img.shape
        Dithered = np.copy(Img)/255
        for i in range(0, Shape[0]):
                for j in range(0, Shape[1]):
                        for k in range (0,Shape[2]):
                                oldPixel = Dithered[i,j,k]
                                newPixel = np.round(oldPixel)
                                error = oldPixel - newPixel
                                Dithered[i,j,k] = newPixel
                                share_error(Dithered[:,:,k], error, i, j)
        
        return np.round(Dithered)