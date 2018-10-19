
'''
investigate mandelbrout fractal 
feel comfortable manipulating pixels 

For each pixel (Px, Py) on the screen, do:
{
  x0 = scaled x coordinate of pixel (scaled to lie in the Mandelbrot X scale (-2.5, 1))
  y0 = scaled y coordinate of pixel (scaled to lie in the Mandelbrot Y scale (-1, 1))
  x = 0.0
  y = 0.0
  iteration = 0
  max_iteration = 1000
  while (x*x + y*y < 2*2  AND  iteration < max_iteration) {
    xtemp = x*x - y*y + x0
    y = 2*x*y + y0
    x = xtemp
    iteration = iteration + 1
  }
  color = palette[iteration]
  plot(Px, Py, color)
}
wikipedia.org
'''


from PIL import Image
import random
import math
import sys


# -2.5 +  3.5 * px
#         ---
#.        511

#  0    1            256                   511
# -2.5  -2.49       -0.75                   1
#points = int(sys.argv[1]) 
imgx = 512 
imgy = 512 

image = Image.new("RGB",(imgx,imgy))

for Px in range(imgx):
	print( str(Px*100.00/imgx) + "%")
	for Py in range(imgy):

		x0 = (3.5/511)* Px + (-2.5) 
		y0= (2/511) * Py + (-1)
		x = 0.0
		y = 0.0
		iteration = 0 
		max_iteration = 1000
		while (x*x + y*y < 2*2) and iteration < max_iteration:
			xtemp = x*x - y*y + x0
			y = 2*x*y + y0
			x = xtemp 
			iteration = iteration + 1 
		colorR = iteration%250
		colorG = iteration%250
		colorB = 0
		image.putpixel((Px,Py),(colorR, colorG, colorB))

image.save("mandelbrout.png", "PNG")
