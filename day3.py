#Numeric datatype --> int,float,complex along with boolean

#Input formatting -->Accepting input from the user --> input

#Accepting integer -->input from user
#by default input() accepts amy input --> str
#int(input()) --> will accept only integers
'''age = int(input('Enter the age:'))
print(age)
print(type(age))

#float (input()) -->accepts integers,float values

age = float(input('Enter the age:'))
print(age)
print(type(age))'''

#Accepting string input from user

'''name = input("Enter the name:")
print(name)
print(type(name))

#Accepting group of values

marks = int(input("Enter the marks:"))
print(marks)
print(type(marks))

a = input().split() #by default split() has space
print(a)


#Space separated values
a = input().split() #now you enter spaces in output
print(a)

#comma separated values
a = input("Enter the values:").split(',')
print(a)

#List of integers
marks = list(map(int,input("Enter the values:").split(',')))
print(marks)
            
#Now we want to accept 2 values from user
age,salary = map(int,input("Enter the values:").split(','))
print(age)
print(salary)'''

'''s#Float of integers
marks = list(map(int,input("Enter the values:").split(',')))
print(marks)

#Single input --> int(input())
#two inputs --> a,b = map(int,(input().split(',')
#any number result as list --> a = list(map(int,input().split(',')))

#group of float values
age,salary = map(float,input("Enter the values:").split(','))
print(age)
print(salary)

marks = list(map(float,input("Enter the values:").split(',')))
print(marks)
'''

'''#Accepting input from user --> int,float -> input formatting

#Operators --> Operators perform operations between values (operands)
#7 types --> Arithmetic,Assignment,Comparision (Relationship)
#Membership,Identity,Logical,Bitwise

#Arithmetic Operators -->Arithmetic operations
#+ , - , *,/
print(5+3)
print(5-2)
print(5*2)
print(5/2) #Float value
#Floor Division (Integer division) -->returns quotient
print(5//2)
#Modulus -->divisble rules ->returns remainder
print(5%2)
#power (exponential)
print(5**2)

#Task -->Accept integer input as length,breadth -->find the area of rectangle
#Area = length * breadth
length = 5
breadth =6
print(length*breadth)

length,breadth = map(int,input("Enter the values:").split(','))
area = length * breadth
print(area)'''


#Assignment operators -->assign the values
# = , += , -+
a = 45
print(a)
#update the value of a
a = a+5 #a+= 5
print(a)
b = 35
b += a #b = b + a
print(b)
b -= 5
print(b)

# Task : *=,/=,//=,%= workout
b *= 5
print(b)
b /= 5
print(b)
b //= 5
print(b)
b %= 5
print(b)

























