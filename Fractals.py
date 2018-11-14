'''
CS550 Fractal Project by KB
10/25/18 
This project includes two interesting mandelbrot fractels and one fractal based loosely on the Cantor set 
It also includes experimentation with colors and other functions availible in the PIL library 
This is a combination of previous work from projects: mandelbrot, mandelbrot2, fractal, and spiral thing, so please see those projects for work progression 

On my honor, I have neither given nor recieved unauthorized aid. 

'''
from PIL import ImageDraw 
from PIL import Image
import random as r
from PIL import ImageColor as I
from PIL import ImageOps
from PIL import ImageFilter

#Recursively drawn line based fractal loosely based on Cantor set. Mainly inspired by image on  Nature of Code website linked below
#Sources: 
#https://natureofcode.com/book/chapter-8-fractals/
#https://stackoverflow.com/questions/13053443/drawing-a-line-on-an-image-with-pil/13053545
#https://stackoverflow.com/questions/9983263/crop-the-image-using-pil-in-python
#Made with some suggestions from an experinced programer 

#set image size
imgx = 1000
imgy = 1000



# Create a new image in HSV color mode
image = Image.new("HSV",(imgx,imgy))
#image drawing function for use of lines
draw = ImageDraw.Draw(image)

#def the draw funciton to be called recursively
def drawOut(x, y, dx, dy, num, den):
	#if the change in distance becomes 0, stop drawing
	if dx == 0 and dy == 0:
		return
	#draw an inital starting line in two directions, random colors using HSV
	draw.line((x, y, x+dx, y+dy), fill=(r.randrange(0,361),100, 200), width = 1)
	draw.line((x, y, x-dx, y-dy), fill=(r.randrange(0,361),100, 200), width = 1)
	#draw a line from the end point of intial line, except at x and y are switched (drawn at a 90 degree angle) in both directions and length is decreased by a certain fraction (num/den). Repeats recusively until length is decreased to zero 
	drawOut(x+dx, y+dy, (num*dy)//den, (num*dx)//den, num, den)
	drawOut(x-dx, y-dy, (num*dy)//den, (num*dx)//den, num, den)

#Initial calling of function, starting lines are drawn at the center of the image. The initial num and dem were chosen after experiementation to produce the most interetesing looking fractal. 23/32 produces the maximum number of lines without overlap. 
drawOut(imgx//2, imgy//2, imgx//6, 0, 23, 32)

#crops image to make the fractal easier to see
area = (imgx*(1/10), imgy *2/10, imgx*9/10, imgy*8/10)
cropped_img = image.crop(area)
#shows image
cropped_img.show()


#Mandelbrot Fractal 

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
		max_iteration = 400
		while (x*x + y*y <= 2) and iteration < max_iteration: 
			#calculations based on wikihow
			xtemp = x*x - y*y + xS
			y = 2*x*y + yS 
			iteration += 1 
			x = xtemp
		# color shades based on iteration and other math to get more interesting images
		colorR = iteration
		colorG = (iteration*50)%256
		colorB = 256- iteration
		image.putpixel((Px,Py),(colorR, colorG, colorB))
		
#Interesting function in ImageOps in PIL that inverts pixels above a certain threshold value, shows image. 
ImageOps.solarize(image, threshold=240).show()

#Mandelbrot 3
xa, xb = -0.6761486325412989, -0.6649729572236538
ya, yb = -0.46341093443341, -0.45223525911569595

imgx = 500
imgy = 500
image = Image.new("HSV",(imgx,imgy))

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
		max_iteration = 400
		while (x*x + y*y <= 2) and iteration < max_iteration: 
			#calculations based on wikihow
			xtemp = x*x - y*y + xS
			y = 2*x*y + yS 
			iteration += 1 
			x = xtemp
		# Played around with colorspace. Although calculation is simple, finding the right combination of ImgX variable, Px variable and the important iteration variable to acheive the desired affect did take much experimentation 
		Color= (iteration%360)%int(360/imgx*Px+1)
		Saturation = 360%int(iteration*2)
		Brightness= 300
		colorB = 256- iteration
		image.putpixel((Px,Py),(Color, Saturation, Brightness))
#shows image 
image.show()

