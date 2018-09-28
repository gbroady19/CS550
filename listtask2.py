import random as r

a=[]
for x in range(15):
	a.append(r.randrange(100))

 
newnumber= int(input("Please input a number from 0-100\n\n>>"))

if  100 >= newnumber:
	a.append(newnumber)

elif 0 <= newnumber:
	a.append(newnumber)

else: 
	print("thats not in the range")
	quit()

print(sorted(a, reverse=True)) 