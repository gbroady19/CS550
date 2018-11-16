#Image filter for CS550
#Produces image with star overlay 
#To produce image, type in filename.jpg when starting program
#Also, please download 
#overlay image from https://favim.com/image/4868965/

from PIL import Image
from PIL import ImageDraw 
from PIL import ImageOps
import sys

imagefile = sys.argv[1]
im = Image.open(imagefile, mode="r")
width=im.width
height = im.height
overlay = Image.open("Stars.jpeg", mode="r")
overlay=overlay.resize((width,height))
Finalimage = Image.blend(im, overlay, 0.25)
Finalimage.show()