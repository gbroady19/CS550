from PIL import Image

imgx = 512 
imgy = 512 

image = Image.new("RGB",(imgx,imgy))

image.putpixel((0,0),(100,0,100))

image.save("demo_image.png", "PNG")
