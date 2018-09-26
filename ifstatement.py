#if statement 
import sys

rawgrade = float(sys.argv[1]) 


if 5 >= rawgrade >= 4.85: 
	print("A+")
elif 4.85 > rawgrade >= 4.7:
	print("A")

elif 4.7 > rawgrade >= 4.5:
	print("A-")

elif 4.5 > rawgrade >= 4.2:
	print("B+")

elif 4.2 > rawgrade >= 3.85:
	print("B")

elif 3.85 > rawgrade >= 3.5:
	print("B-")

elif 3.5 > rawgrade >= 3.2:
	print("C+")

elif 3.2 > rawgrade >= 2.85:
	print("C")

elif 2.85 > rawgrade >= 2.5:
	print("C-")

elif 2.5 > rawgrade >= 2:
	print("D+")

elif 2 > rawgrade >= 1.5:
	print("D")
elif 1.5 > rawgrade >= 1:
	print("D-")

elif 1 > rawgrade >= 0:
	print("F")

else: 
	print("I don't know what that means")
	quit()