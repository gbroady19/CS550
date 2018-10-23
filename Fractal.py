#Fractal Drawing 
#https://natureofcode.com/book/chapter-8-fractals/
#https://stackoverflow.com/questions/13053443/drawing-a-line-on-an-image-with-pil/13053545

from PIL import ImageDraw 
from PIL import Image
import random as r

imgx = 1000
imgy = 1000

image = Image.new("RGB",(imgx,imgy))
draw = ImageDraw.Draw(image) 


'''
void cantor(float x, float y, float len) {
Stop at 1 pixel!
  if (len >= 1) {
    line(x,y,x+len,y);
    y += 20;
    cantor(x,y,len/3);
    cantor(x+len*2/3,y,len/3);
  }
}
'''


def pattern(x,y,length):
	if length > 1:
		draw.line((x,y,x+length, y), fill=(r.randrange(0,256), r.randrange(0,256), r.randrange(0,256)), width = 3)
		y += 20;
		pattern(x,y,length/3) 
		pattern(x+length*2/3,y,length/3)



# newy=10 + y
# while newy < 1000:

# 	newy = 
pattern(0,0,1000)
pattern(0,100, 1000)
pattern(0,200, 1000)
pattern(0,300, 1000)
pattern(0,400, 1000)
pattern(0,500, 1000)
pattern(0,600, 1000)
pattern(0,700, 1000)
pattern(0,800, 1000)

image.show()



