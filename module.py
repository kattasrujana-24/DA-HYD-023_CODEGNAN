import AUG29 
print(dir(AUG29))
'''print(type(AUG29.details))
print(type(AUG29.greeting))

print(AUG29.greeting())
print(AUG29.details)
#we can access funcitons/datatypes using . operator

AUG29.details['subjects'] = ['Python','SQL','EDA', 'PowerBI','Excel']
print(AUG29.details.keys())'''
'''
#we can use from keyword to access desired methods/datatypes
from AUG29 import details
print(details)
#print(greeting()) #as we didn't import it raises NameError

details['subjects'] = ['Python','SQL','EDA', 'PowerBI','Excel']
print(details)

from AUG29 import details,greeting
print(greeting())
print(details)

#you want to access all functions from a module at a time
# * is recommended only for user defined values
from AUG29 import *
print(details)
print(greeting())

#Aliasing --> we use keyword as shortcut for original file
import AUG29 as mod
print(mod.details)

#we will work on some built-in modules --> random, math
import random
import time
#random module --> get random number generation, random rext
print(dir(random))
#OTP generation
#print(random.randint(1,10))
for i in range(5):
    print(random.randint(1000,9999)) #start limit, endlimit
    time.sleep(5) #delays execution sleep(second)

print(random.random()) #returns a float value of random 

details = ['A long back','Once upon a time','Ten years ago']
print(random.choice(details)) 

#you can try for story generation
'''
#math module --> Mathematical constants,log,exp,trignometric....

import math
#print(dir(math))
print(math.ceil(4.5)) #it returns the next highest value
print(math.floor(4.78))
print(math.factorial(5))
print(math.pi)
print(math.gcd(5,3)) 
print(math.trunc(4.95))

