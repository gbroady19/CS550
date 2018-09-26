import sys
import math

x = float(sys.argv [1])
y = float(sys.argv [2])
z = float(sys.argv [3])

if (x>y>z) or (x<y<z):
	print('true')
else:
	print("false")

