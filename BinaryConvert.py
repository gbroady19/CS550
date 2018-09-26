#Binary Convert
import sys 

input = (sys.argv[1])
total=0
for x in range(len(input)):
	d=int(input[len(input)-x-1])*(2**(x))
	total += d

print(total)