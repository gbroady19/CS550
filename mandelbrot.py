#mandelbrot by KB for CS550
#inspired by work done with wikipedia example code
from PIL import Image 
import random 

#set image size
imgx = 500
imgy = 500

image = Image.new("RGB",(imgx,imgy))

#for all the pixels in the image
for Px in range(imgx):
	for Py in range(imgy):
		#divide all the pixels into sections between -2 and 2
		xS = (4/(imgx-1))* Px + (-2) 
		yS= (4/(imgy-1)) * Py + (-2)
		x = 0 
		y = 0 
		iteration = 0 
		#set maximum number of iterations
		max_iteration = 250
		while (x*x + y*y <= 2) and iteration < max_iteration: 
			#calculations based on wikihow
			xtemp = x*x - y*y + xS
			y = 2*x*y + yS 
			iteration += 1 
			x = xtemp
		# color shades based on iteration 
		colorR = iteration
		colorG = 0
		colorB = 0
		image.putpixel((Px,Py),(colorR, colorG, colorB))


image.save("mandelbrot.png", "PNG")




