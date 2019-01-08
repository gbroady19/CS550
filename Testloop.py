for j in range(7):
  for i in range(7): 
    if j==0 or j==6 or i==0 or i==6:
       print('# ',end='')
    else:
      print('  ',end='')
  print('')

print('')

for j in range(7):
  for i in range(7): 
    if j==0 or j==6 or j==i or i+j==6:
      print('# ',end='')
    else:
      print('  ',end='')
  print('')

print('')

for j in range(7):
  for i in range(7): 
    if j==0 or j==6 or j==i or 6-i==j or i == 0 or i==6:
      print('# ',end='')
    else:
      print('  ',end='')
  print('')


# 6,1    7-i,j
#5,2
#4,3
#3,4
#2,5
# 1,6
#




#num = []
# for x in range(1,111):
# 	if (x%3==0) and (x%5 == 0):
# 		x = "CozaLoza"
		
		
# 	elif (x%3==0) and (x%7==0):
# 		x = "CozaWoza"
		
		
# 	elif (x%5==0) and (x%7==0):
# 		x = "LozaWoza"
	
		
# 	elif x%3 == 0: 
# 		x = "Coza"
		
		
# 	elif x%5 == 0:
# 		x = "Loza"
		
		
# 	elif x%7 == 0:
# 		x = "Woza"
		
	
# 	num.append(x)

# for i in range(0, len(num), 11):
#     print(num[i:i + 11])
