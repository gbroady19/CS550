#mandelbrot by KB for CS550
#inspired by work done with wikipedia example code
from PIL import Image 
import random 

#set image size
imgx = 1000
imgy = 1000

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
		image.putpixel((Px,Py),(colorR, (colorG), colorB))


image.save("mandelbrot2.png", "PNG")




