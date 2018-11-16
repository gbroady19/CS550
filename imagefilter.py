
#CS550 Filter by KB 
#Produces purple colorized image 
#To produce image, type in filename.jpg when starting program


from PIL import Image
from PIL import ImageDraw 
from PIL import ImageOps
import sys

imagefile = sys.argv[1]
im = Image.open(imagefile)
image=ImageOps.grayscale(im) #converts image to grayscale
color=ImageOps.colorize(image,(204,204,255),(51,0,51)) #colorizes image 
color.show() #show image 
