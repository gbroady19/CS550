#Task 1
import random as r

a=[]
for x in range(10):
	a.append(r.randrange(100))
	a.sort()
for x in a:
	if x % 3 == 0: 
		a.remove(x)

print(a)

#got help from: https://thispointer.com/python-how-to-remove-multiple-elements-from-list/

