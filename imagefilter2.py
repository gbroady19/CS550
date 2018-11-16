
from PIL import Image
from PIL import ImageDraw 
from PIL import ImageOps
import sys

imagefile = sys.argv[1]
im = Image.open(imagefile)
width=im.width
height = im.height
overlay = Image.open("Stars.jpg")
overlay.resize((width,height))
Finalimage = Image.blend(im, overlay, 0.5)