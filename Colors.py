#10/13/18 
#HW for CS550 HO 
from PIL import ImageMath
from PIL import Image


imgx = 512 
imgy = 512 

image = Image.new("RGB",(imgx,imgy))
#https://stackoverflow.com/questions/30608035/plot-circular-gradients-using-pil-in-python
#I solved the "make a red image" problem first, so I did not intend for this link to complete the entire assignment nor did i directly copy from it


innerColor = (200)
innerColor2= (100)
innerColor3= (50)

outerColor= (100)
outerColor2=(150)
outerColor3=(200)


for x in range(imgx):
	for y in range(imgy):
						#Distance to endge, subtracted from, Greatest value of distance to edge calculation 
		distanceToEdge = max(abs(x - imgx), x, abs(y - imgy), y)- min(abs(x - imgx), x, abs(y - imgy), y)
		
		#Make it on a scale from 0 to 1 to allow for a smootth transition 
		distanceToEdge = float(distanceToEdge) / (imgx/2)

       


        #Calculate r, g, and b values that allow the inner color to slowly become outer color. as the distance to edge becomes closer to zero
        #the innercolor value gets closer to zero, so the number approaches the outer color. 
		r = innerColor * distanceToEdge + outerColor * (1 - distanceToEdge)
		g = innerColor2 * distanceToEdge + outerColor2 * (1- distanceToEdge)
		b = innerColor3 * distanceToEdge + outerColor3 * (1 - distanceToEdge)


        #Place the pixel        
		image.putpixel((x, y), (int(r), int(g), int(b)))

image.save("Gradientdemo.png","PNG")
