import random as r 

#empty list
a = []

#add something to list 
a.append(4)
a.append(5)
a.append(3)
a.append(3)
a.insert(1,1)

print(a[0],a[4])

b = [1,1,4,5,3]
b.remove(1)
del b[0]

print(b.pop())
print(b)


print(b[len(b)-1])
print(b[-1])

c=5
d=7

c,d=d,c 

c,d= 5,7 #swap

#swap 
temp = c
c= d 
d= temp

e = [1,2,3,4,5,6,4]

#e[2],e[6] = e,[6], e[2]

f=[]
for x in range(7, 701, 7): 
	f.append(x) 

print(f)
print(len(f))

g=[]
for x in range(10): 
	g.append(r.randrange(100))
 	
g.sort() 

print(sorted(g))









