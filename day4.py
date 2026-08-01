'''
Identity Operators --> checks the identity of an object --> id()
#is,is not
'''
'''
a = 5
b = a
print(id(a))
print(id(b))
c = 5
print(id(c))
print(a is c)
print(5 ==5)

a = [1,3,5,6]
b = a
print(id(a))
print(id(b))
c = [1,3,5,6]
print(id(c))
#As we have Lists (Mutable Collection) both c and a lists will have different i
#ids whereas values are same
print(c is a)
print(c == a)
print(a is not c)


#Bitwise Operators --> we perform bitwise operations over operands
#& (and), | (or), ^(XOR), shifting operators (<<,>>)
#Number will be converted to binary format

print(5&3) #both 5 and 3 to be converted binary and bitwise and is performed

print(5|3) #bitwise OR

print(5^3) #bitwise XOR

print(5 and 3) #here and is logical operator checks for both existances
#returns 5 in above case

print(5 or 3) #returns 3 in this case

#Leftshift operator << , Rightshift operator >>

print(5 < 1) #False Comparision
print(5 << 1) #Left shift operation by 1 position
print(5 >> 1) #Right shift operation by 1 position

print(15 << 2) #converting 15 to binary and performs 2 times left shifting

print(15 >> 2) #2 times right shifting

#Input Formatting --> input(),int(input()),float(input())
#You Know -->single input
#2 or 3 inputs --> map()
#group of integers --> list(map(int,input().split(','))

names = input("Enter the names:").split(',')
print(names)

name1,name2 = map(str,input("Enter the names:").split(','))
print(name1,name2)
'''
#Tokens --> Numeric Datatypes --> Operators -->Flow of the program
#Control Block Statements --> they control the flow of the program
#When to execute,how to execute
#Conditional Statements --> if,else,elif (rely on condition to be executed)
#Repetition Statements (Loops) --> for,while
'''
Syntax :
  
if <condition>:
    statement(s)...
    ....

#age = 15
age = int(input("Enter the age:"))
if age >=18:
    print('Your age is:',age)
  
age = int(input("Enter the age:"))
if age>=18 and age in [19,21,20]:
    print('Your Age is',age)
    print(age)


#else keyword --> if-else

else:
    statement(s)...
else:
    statement(s)....
    
if-else is used as below

if <condition>:
    statement(s)...
    
else:
    statememt(s)...
    


#Vote Eligibility -->To chech his/her voter eligibility and give access...

age = int(input("Enter the age:"))
if age>=18:
    print("You have voter eligibility and age is",age)
    print("Access Granted")
else:
    age = 18-age
    print("You dont have eligibility as your age is",age,"Years")
    print("You need to wait for more",age,"Years")

#same case let's use only nested --> if,else
if age >0:
    if age>=18:
        print("You have voter eligibility and age is",age)
        print("Access Granted")
    else:
        age = 18-age
        #print("You dont have eligibility as your age is",age,"Years")
        print("You need to wait for more",age,"Years")
else:
    print("You have entered -ve values/Zero enter only +ve")

      
task : Student marks and grade analyzer
90-100 --> 'A'
80-89 --> 'B'
70-79 --> 'C'
60-69 --> 'D'
<60 -->Fail
#also -ve cases should not be allowed and marks souldnt be greater than 100

'''
#Students Marks and Grade Analyzer

marks = int(input("Enter the marks:"))
if marks < 0 or marks >100:
    print("Invalid marks! please enter marks between 0 to 100")

if marks >= 90:
    print("Grade: A")
    
 '''   
if marks >= 80:
    print("Grade: B")
    
if marks >= 70:
    print("Grade: C")

if marks >= 60:
    print("Grade: C")

else:
    print("Fail")
'''










