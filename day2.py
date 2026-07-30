'''
Tokens -> Variables,Punctuatiors

Variables -> Named memory location, its a laceholder for data
#Rules are to be followed
'''

#MultiAssignment of Variables

name,age,place = 'Codegnan',7,'Hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='---->')

#a,b = 2,4,5 #ValueError as too many values to unpack

name = "Codegnan"
a,b = 45,1.5
print(a,b)
a,b = b,a #swapping
print(a,b,sep=',')

#a,b = b,c #NameError as 'c' id not defined
#rint(a,b)

#Deleting the variables -<del
#del a
#print(a)
#del 
#print(a,b)

#Punctuators -> [](Lists),()(tuples),{}(Dict,Sets)
name = "Codegnan";age = 7;course = 'Data_Analytics'
print(name,age,course)

#Datatypes -> Numeric (int,float,complex),boolean,None,
         #->Sequences ->Lists,Tuples,Sets,Strings,Frozensets,mappings(dict)

#Numeric datatype ->int,float,complex

#int datatype ->quality,age
age = 7
print(age)
print(type(age)) #type -> returns the datatype of object

print(type(234))
'''

#quantity = 03 #it is not allowed
#print(quantity)

#float datatype -> temp,salary,price
price = 750.24;discount = 2.5
print(price,discount)
print(type(price))
'''

#complex ->Combination of real and imag
i2 = 4
data = 5+i2
print(data)

data = 5+2j #j is imag representation
print(data)
print(type(data))


#Boolean -> True/False

valid = True
print(type(valid))

error = False
print(type(error))

#Typecasting -> Converting one type to another type
#Python by default follows Implicit Type (WE need not mention the datatype)

#Explicit
#int,float,complex,bool

#Typecasting -> int ->float,complex,bool

age = 35
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d = bool(age)
print(d)
e = bool(0)
print(e)

#Float ->Typecasting

age = 35.4
print(type(age))
b = int(age)
print(b)
c = complex(age)
print(c)
d = bool(age)
print(d)
e = bool(1)
print(e)

#Complex ->Typecasting ->int,float,bool
data = 2+5j
print(type(data))
a = int(data)
print(data)
'''
b = float(data)
print(data)
c = bool(data)
print(c)
print(type(c))


e = int(float(bool(45)))
print(e)






















