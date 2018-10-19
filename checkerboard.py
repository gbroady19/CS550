from PIL import Image 
import random 

imgx = 512 
imgy = 512

image = Image.new("RGB",(imgx,imgy))

'''

  0 1 2 3 4 5
0 x   x
1   x   x
2 x   x
3
4
5


'''

randomcolorR = random.randrange(0,250)
randomcolorG = random.randrange(0,250)
randomcolorB = random.randrange(0,250)
for x in range(imgx):
	for y in range(imgy):
		
		if ((x//64)%2 == 1) and ((y//64)%2 == 0) or ((y//64)%2 == 1) and ((x//64)%2 == 0):
			image.putpixel ((x,y),(0,0,0)) 

		else: 
			image.putpixel((x,y),(randomcolorR,randomcolorG,randomcolorB)) 

image.save("Checkboard.png","PNG")
