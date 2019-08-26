import cv
from random import randint


def quantize(name, depth):
	img = cv.LoadImage(name, cv.CV_LOAD_IMAGE_GRAYSCALE)#cv.CV_LOAD_IMAGE_COLOR
	x,y = cv.GetSize(img)
	out = cv.CreateImage((x,y),8,1)#((w,h), depth, channels)

	mask = int("".join(["1" if n<depth else "0" for n in xrange(8)]),2)

	for i in xrange(x):
		for j in xrange(y):
			out[j,i] = mask & int(img[j,i]+0.5)

	cv.ShowImage("quantize "+str(depth), out)
	cv.MoveWindow("quantize "+str(depth), 0, 0)
	cv.SaveImage("quantize_"+str(depth)+"_"+name.split(".")[0]+".png", out)
	cv.WaitKey(0)

def random_dither(name):
	img = cv.LoadImage(name, cv.CV_LOAD_IMAGE_GRAYSCALE)
	x,y = cv.GetSize(img)
	out = cv.CreateImage((x,y),8,1)

	for i in xrange(x):
		for j in xrange(y):
			if randint(0,255)<img[j,i]:
				out[j,i] = 255
			else:
				out[j,i] = 0

	cv.ShowImage("random_dither", out)
	cv.MoveWindow("random_dither", 0, 0)
	cv.SaveImage("random_dither_"+name.split(".")[0]+".png", out)
	cv.WaitKey(0)

def ordered_dither(name):
	img = cv.LoadImage(name, cv.CV_LOAD_IMAGE_GRAYSCALE)
	x,y = cv.GetSize(img)
	out = cv.CreateImage((x,y),8,1)

	d = [[3,1],[0,2]]
#	d = [[1,9,3,11],[13,5,15,7],[4,12,2,10],[16,8,14,6]]
	n = len(d)

	for i in xrange(x):
		for j in xrange(y):
			if d[i%n][j%n]>(((n*n-0)*(img[j,i]-0))/(255-0))+0:
				out[j,i] = 0
			else:
				out[j,i] = 255

	cv.ShowImage("ordered_dither", out)
	cv.MoveWindow("ordered_dither", 0, 0)
	cv.SaveImage("ordered_dither_"+name.split(".")[0]+".png", out)
	cv.WaitKey(0)

def error_dither(name):
	img = cv.LoadImage(name, cv.CV_LOAD_IMAGE_GRAYSCALE)
	x,y = cv.GetSize(img)
	
	for i in xrange(x):
		for j in xrange(y):
			closest = 255 if img[j,i]>(255.0/2) else 0
			error = img[j,i]-closest
			img[j,i] = closest
			if i<x-1:
				img[j,i+1] += (7.0*error)/16.0
			if i>0 and j<y-1:
				img[j+1,i-1] += (3.0*error)/16.0
			if j<y-1:
				img[j+1,i] += (5.0*error)/16.0
			if i<x-1 and j<y-1:
				img[j+1,i+1] += (1.0*error)/16.0

	cv.ShowImage("error_dither", img)
	cv.MoveWindow("error_dither", 0, 0)
	cv.SaveImage("error_dither_"+name.split(".")[0]+".png", out)
	cv.WaitKey(0)

def show_all(name):
	quantize(name, 8)
	quantize(name, 4)
	quantize(name, 2)
	quantize(name, 1)
	random_dither(name)
	ordered_dither(name)
	error_dither(name)


if __name__=="__main__":
#	name = "cube.jpg"
	name = "lena.png"
	show_all(name)

