from PIL import Image

imgx = 512 
imgy = 512 

image = Image.new("RGB",(imgx,imgy))


for x in range(imgx):
	for y in range(imgy):
		if ((x//64)%2 == 1) or ((x//64)%2 == 2) and (y//64)%2 == 1 or ((y//64)%2 == 2):
			image.putpixel ((x,y), (0,0,0) )
		else: 
			image.putpixel ((x,y), (250,0,0) )

image.save("demo_image.png", "PNG")
