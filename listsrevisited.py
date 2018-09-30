i = [[1,2,3],[4,5,6], [7,8,9 ]]
i[0][0]

print(i[2][0])

j = [0] * 10

print(j)

a = []
for x in range(10):
	k = [0] * 10
	a.append(k)

print(a)

a = [[0] * 10 for x in range(10)]
print(a)

for x in range(len(a)): 
	print(*a[x])

#python 3 ms.py w h b 