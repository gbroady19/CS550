# from PIL import Image
# from PIL import ImageFilter
# from PIL import ImageEnhance
# im = Image.open("SRP.jpg")
# im = im.filter(ImageFilter.MaxFilter(3.3))
# im,
# im.show()
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from PIL import ImageOps

im = Image.open("grass.jpg")
width=im.width
height = im.height
tint=Image.new("RGB",(width,height),(300,100,100))
image=ImageOps.grayscale(im)
color=ImageOps.colorize(image,(204,204,255),(51,0,51))
color.show()
# finalimage=Image.blend(color,tint,0.25)
# finalimage.show()
