#Programming Tasks
import sys
import math

t = float(sys.argv [1])
v= float( sys.argv [2])

result= (35.74  +  0.6215*t  +  (0.4275*t  -  35.75)*(v**0.16))
print(result)
