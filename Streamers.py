from PIL import Image
import random
import math
import sys

streamers = int(sys.argv[1]) 
imgx = 512 
imgy = 512 

image = Image.new("RGB",(imgx,imgy))

for j in range(streamers): 

	randomcolorR = random.randrange(0,250)
	randomcolorG = random.randrange(0,250)
	randomcolorB = random.randrange(0,250)
	x = random.randrange(imgx)
	for y in range(imgy):
		x = x+random.randrange(-1,2)
		if x> 511: 
			x = - 1
		if x < 0:
			x = + 1
		image.putpixel((x,y),(randomcolorR,randomcolorG,randomcolorB))

image.save("streamers.png", "PNG")
