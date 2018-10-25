
from PIL import ImageDraw 
from PIL import Image
import random as r
from PIL import ImageColor as I
from PIL import ImageOps 
#https://stackoverflow.com/questions/9983263/crop-the-image-using-pil-in-python

imgx = 2000
imgy = 2000

image = Image.new("HSV",(imgx,imgy))
draw = ImageDraw.Draw(image) 

def drawOut(x, y, dx, dy, num, den):
	if dx == 0 and dy == 0:
		return
	draw.line((x, y, x+dx, y+dy), fill=(r.randrange(0,361),100, 200), width = 1)
	draw.line((x, y, x-dx, y-dy), fill=(r.randrange(0,361),100, 200), width = 1)
	drawOut(x+dx, y+dy, (num*dy)//den, (num*dx)//den, num, den)
	drawOut(x-dx, y-dy, (num*dy)//den, (num*dx)//den, num, den)

drawOut(imgx//2, imgy//2, imgx//6, 0, 23, 32)

area = (imgx*(1/10), imgy *2/10, imgx*9/10, imgy*8/10)
cropped_img = image.crop(area)
cropped_img.show()

import random 
from PIL import ImageFilter
#set image size
imgx = 500
imgy = 500


xa, xb = -0.75029467235117, -0.7478726919928045
ya, yb = 0.06084172052354717, 0.06326370066585434
image = Image.new("RGB",(imgx,imgy))

#for all the pixels in the image
for Py in range(imgy):
	yS= ((yb-ya)/(imgy-1)) * Py + (ya)
	for Px in range(imgx):
		#divide all the pixels into sections between -2 and 2
		xS = ((xb-xa)/(imgx-1))* Px + (xa) 
		x = 0 
		y = 0 
		iteration = 0 
		#set maximum number of iterations
		max_iteration = 256
		while (x*x + y*y <= 2) and iteration < max_iteration: 
			#calculations based on wikihow
			xtemp = x*x - y*y + xS
			y = 2*x*y + yS 
			iteration += 1 
			x = xtemp
		# color shades based on iteration 
		colorR = iteration
		colorG = (iteration*50)%256
		colorB = 256- iteration
		image.putpixel((Px,Py),(colorR, colorG, colorB))
		
	
		
imageed = image.filter(ImageFilter.CONTOUR)
imageedit.save("mandelbrot2.png", "PNG")

