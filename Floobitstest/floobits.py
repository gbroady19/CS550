
# Partner 1: Knute
# Partner 2: Kevin

''' Instructions:
   Work with a partner to complete these tasks. Assume that all variables are declared; you need only write the if-statement using the variables indicated in the description. Write your solution below the commented description.
'''
 
''' 1. 
   Variable grade is a character. If it is an A, print good work. 
'''
if grade == "A":
  print("good work")
 
 
''' 2. 
   Variable yards is an int. If it is less than 17, multiply yards by 2. 
'''
if yards<=17:
   yards = yards*2
 
 
''' 3. 
   Variable success is a boolean. If something is a success, print congratulations. 
'''
if success==True:
   print("congratulations")
 
 
''' 4. 
   Variable word is a String. If the string's second letter is 'f', print fun. 
'''
if word[2]=="f":
   print("fun")
 
 
''' 5. 
   Variable temp is a float. Variable celsius is a boolean. If celsius is true, convert to fahrenheit, storing the result in temp. F = 1.8C + 32.
'''
if celsius == True:
  temp = 1.8*(temp)+32
 
 
''' 6. 
   Variable numItems is an int. Variable averageCost and totalCost are floats. If there are items, calculate the average cost. If there are no items, print no items.
'''

if numItems>0:
   averageCost = totalCost/numItems
else:
   print("no items")
 
''' 7. 
   Variable pollution is a float. Variable cutoff is a float. If pollution is less than the cutoff, print safe condition. If pollution is greater than or equal to cutoff, print unsafe condition. 
'''
if polution < cutoff:
  print("SAFE")
else: 
  print("UNSAFE") 

 
''' 8. 
   Variable score is a float, and grade is a char. Store the appropriate letter grade in the grade variable according to this chart.
   F: <60; B: 80-89; D: 60-69; A: 90-100; C: 70-79.
'''

if score<60:
   grade = "F":
elif score<69:
   grade = "D"
elif score<79:
   grade = "C"
elif score<89:
   grade = "B"
else:
   grade = "A"
 
''' 9.
   Variable letter is a char. If it is a lowercase letter, print lowercase. If it is an uppercase, print uppercase. If it is 0-9, print digit. If it is none of these, print symbol.
'''
if char.isupper() == True:
   print("uppercase")
elif char.islower()== True: 
   print("lowercase")
elif char.isdigit() == True:
   print("digit")
else:
   print("symbol")

 
''' 10. 
   Variable neighbors is an int. Determine where you live based on your neighbors.
   50+: city; 25+: suburbia; 1+: rural; 0: middle of nowhere. 
'''
 
if neighbors==0:
   print("middle of nowhere")
elif neighbors<25:
   print("rural")
elif neighbors<50:
   print("suburbs")
else:
   print("city")

''' 11. 
   Variables doesSignificantWork, makesBreakthrough, and nobelPrizeCandidate are booleans. A nobel prize winner does significant work and makes a break through. Store true in nobelPrizeCandidate if they merit the award and false if they don't. 
'''

if doesSignificantWork ==True and makesBreakthrough ==True:
   nobelPrizeCandidate = True
else:
   nobelPrizeCandidate = False
 
''' 12. 
   Variable tax is a boolean, price and taxRate are floats. If there is tax, update price to reflect the tax you must pay.
'''
if tax == True: 
   price += taxRate * price

''' 13.  
   Variable word and type are Strings. Determine (not super accurately) what kind of word it is by looking at how it ends. 
   -ly: adverb; -ing; gerund; -s: plural; something else: error   
'''
try:
   if word[-1]=="s":
      type = "plural"
   elif word[-1]+word[-2]=="ly":
      type = "adverb"
   elif word[-1]+word[-2]+word[-3]=="ing":
      type = "gerund"
   else:
      type = "error"
except:
   if type==None:
      type="error"
 
''' 14. 
   If integer variable currentNumber is odd, change its value so that it is now 3 times currentNumber plus 1, otherwise change its value so that it is now half of currentNumber (rounded down when currentNumber is odd). 
'''
 if (currentNumber%2) == 1: 
   currentNumber = (currentNumber*3)+1 
 else: 
   currentNumber = (currentNumber//2)
 
''' 15. 
   Assign true to the boolean variable leapYear if the integer variable year is a leap year. (A leap year is a multiple of 4, and if it is a multiple of 100, it must also be a multiple of 400.) 
'''
if year%4==0:
   leapYear=True
   if year%100==0 and year%400!=0:
      leapYear=False
else:
   leapYear=False

''' 16. 
   Determine the smallest of three ints, a, b and c. Store the smallest one of the three in int result. 
'''
result = min(a,b,c)
 
''' 17. 
   If an int, number, is even, a muliple of 5, and in the range of -100 to 100, then it is a special number. Store whether a number is special or not in the boolean variable special. 
'''
if number%2==0 and number%5==0 and -100<number<100:
   special=True
else:
   special=False
 
''' 18. 
   Variable letter is a char. Determine if the character is a vowel or not by storing a letter code in the int variable code.
   a/e/o/u/i: 1; y: -1; everything else: 0
'''
if letter in "aeiouAEIOU":
   code=1
elif letter == "y":
   code=-1
else:
   code=0

 
''' 19. 
   Given a string dayOfWeek, determine if it is the weekend. Store the result in boolean isWeekend.
'''
 if dayOfWeek.title() in ["Saturday","Sunday"]:
   isWeekend = True 
 else:
   isWeekend = False 
 
 
''' 20. 
   Given a String variable month, store the number of days in the given month in integer variable numDays. 
'''

if month.title() in ["January", "March", "May", "July", "August", "October", "December"]:
   numDays = 31
elif month.title() in ["April", "June", "September", "November"]:
   numDays = 30
else:
   numDays = 28
 
 
''' 21. 
   Three integers, angle1, angle2, and angle3, supposedly made a triangle. Store whether the three given angles make a valid triangle in boolean variable validTriangle.
'''
 if (angle1 + angle2 + angle3) == 180: 
   validTriangle = True 
 else: 
   validTriangle = False 
 
 
''' 22. 
   Given an integer, electricity, determine someone's monthly electric bill, float payment, following the rubric below. 
   First 50 units: 50 cents/unit
   Next 100 units: 75 cents/unit
   Next 100 units: 1.20/unit
   For units above 250: 1.50/unit, plus an additional 20% surcharge.
'''
if electricity<=50:
   payment=float(electricity)*0.5
elif electricity<=150:
   payment=25+float(electricity-50)*.75
elif electricity<=250:
   payment=25+75+float(electricity-150)*1.2
else:
   payment=1.2*(1.5*float(electricity))
 
''' 23.
   String, greeting, stores a greeting. String language stores the language. If the language is English, greeting is Hello. If the language is French, the greeting is Bonjour. If the language is Spanish, the greeting is Hola. If the language is something else, the greeting is something of your choice.
'''
 if language.title() == "English":
   greeting = "Hello"
 elif language.title() == "French":
   greeting = "Bonjour" 
 elif language.title() = "Spanish":
   greeting = "Hola"
 else: 
   greeting = "I do not recognize this language"
 
 
''' 24. 
   Generate a phrase and store it in String phrase, given an int number and a String noun. Here are some sample phrases:
   number: 5; noun: dog; phrase: 5 dogs
   number: 1; noun: cat; phrase: 1 cat
   number: 0; noun: elephant; phrase: 0 elephants
   number: 3; noun: human; phrase: 3 humans
   number: 1; noun: home; phrase: 3 homes
'''
if number>1 or number==0:
   phrase = str(number),noun+"s"
else:
   phrase = str(number),noun
 
''' 25. 
   If a string, userInput, is bacon, print out, "Why did you type bacon?". If it is not bacon, print out, "I like bacon." 
'''
 if userInput == "bacon":
   print("Why did you type bacon?") 
 else: 
   print("I like bacon.")
 
''' 26.
   Come up with your own creative tasks someone could complete to practice if-statements. Also provide solutions.
'''


''' Task 1: 
If int, sleep, is less than 6 print "I'm sleepy", else print "I'm ready for the day" 
'''
 
# solution
 if sleep < 6: 
   print("I'm sleepy")
else: 
   print("I'm ready for the day!!")
 
 
''' Task 2:
If a character, letter, comes after R in the alphabet, set boolean isLate to true and set float percent to the character's place in the alphabet divided by 26 (percent of the alphabet surpassed). If not, isLate is false and print "too early"
'''

#solution
if letter in "rRsStTuUvVwWxXyYzZ":
   isLate =True
   alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   percent = (float(alphabet.index(letter.lower())+1))/26
else:
   isLate =False
   print("too early")
 
 
''' Task 3:
A truck needs to know whether it will fit under a low bridge. If int truckheight is less than int bridgeheight then print that it is safe. If it is not safe, print that it is not and print how much the truck would need to be lowered to pass. 
'''
 
# solution
 
if truckheight < bridgeheight: 
   print("safe") 
else: 
   print("unsafe, lower the truck by" + str(truckheight-bridgeheight)) 
 
 
''' Sources
 http://www.bowdoin.edu/~ltoma/teaching/cs107/spring05/Lectures/allif.pdf
 http://www.codeforwin.in/2015/05/if-else-programming-practice.html
 Ben Dreier for pointing out some creative boolean solutions.
'''