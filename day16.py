'''
Functions -->Argument Usage (Variable length arguments)
          -->Keyword variable length arguments (**kwargs)

Exception Handling / Scope of variables / Built-in Functions

Exception Handling -->It is a mechanism that helps to respond or make the flow of execution in normal way,without
this errors will occur and dirupt the flow of program

Common Exceptions -->Value Error,TypeError,IndexError,AttributeError,ZeroDivisionError...

Syntax:

try:
    #code that will cause the exception
except Exception as e:
    #code will catch the exception
finally:
    #runs irrespective of try/except...
    ....
'''
'''
#basic exception handling
try:
    
    #a = 10
    a = int(input("Enter the value:"))
    result =20/a
    print(result)
    print(result) #check for NameError
#except Exception as e:
    #print(e) #it returns the msg of error
except ValueError: #check by changing case
    print(f'Invalid entry enter only integer values')
except ZeroDivisionError:
    print(f'Division by zero is not possible')
except NameError:
    print(f'Check the name of variable properly')



try:
    a = [10,20,30]
    a.append(24)
    print(a[5])
    
    #a = ([12,13,14])
    #print(a[4])
except Exception as e:
    #print(e)

def sample(*a,**b):
    """"Usage of both variable length and keyword variable length args"""
    result = 0
    for i in a:
        if type(i) in (int,float,complex):
            reult = result + i
    print(result)
    return result
    for key,value in b.items():
        print(f'key is {key}')
        print(f'vlaue is {value}')
    return result
sample(2,4,5,'police','codegnan',3,5,name="codegnan",place="hyd",batch= "da23")        

try:
    a=[10,20,30]
    #a.append(24)
    print(a[5])
#except Exception as e:
    #print(e) #returns the msg of the error
except(IndexError,AttributeError) as e:
    print(e)
    a = list(map(int,input("Enter").split(',')))
    print(a)

#BMI --> bmi = (weight) / ((height)**2)
#Feet --> 12 inches--> 1 inch -> 2.54cm
while True:
    try:
        weight = int(input("Enter the weight in kgs:"))
        height = float(input("Enter the height in metres:"))
        #write my logical condition
        if weight > 0 and height > 0:
            break #stops the flow of execution of program
            #continue #skips the current iteration and proceed for rmng iteration
            #print("bye")
        else:
            print("Make sure to enter only correct values")
    except ValueError:
          print(f'Make sure to enter weight as integer only,\ height also a number')
bmi = ((weight) / (height)**2)
print(bmi)          

#Use Exception Handlinf along with Jumping Statement in Functions  BMI Task
'''

#Scope of Variable -->Scope is basically the region/area where it is accesible
#Local Scope,Global Scope
#Global Keyword,Enclosing Scope(Nested Functions nonlocal keyword)
'''
#Local Scope -->Variables defined inside the function accessible inside 

def display():
    """Usage of Local Scope"""
    name= "Codegnan" #local variable
    print(name)
display()
#print(name) #it raises NameError


#Global Scope(variables) -->Defined outside and can be  accessed anywhere in the script

place = "Hyderabad" #global variable
def display():
    """Usage of Local&Global Scope"""
    name = "Codegnan" #local variable
    print(name)
    print(f'{name} is in {place}')
display()
print(place)

#Modifying global variable inside the funciton and accessible outside the function
count = 20
def data():
    """Usage of global keyword"""
    global count
    count = count + 5
    print(f'Value inside function is {count}')
data()
print(f'Value outside function is {count}')


count = 20
def data():
    """Priority of local vs global variable"""
    count = 5 #local variable
    count = count + 5
    print(f'Value inside function is {count}')
data()
print(f'Value outside function is {count}')
'''
'''
#Enclosing Scope (nonlocal keyword)

def outer():
    """Outer function with local variable"""
    count = 5
    def inner():
        """Nested Function"""
        nonlocal count
        count = count + 10
        print(f'Value inside is {count}')
    inner()
    print(f'Value outside is {count}')
outer()    
'''
#Built-in functions -->variables BuiltinScope
len = 56
print(len+4)

print(len('codegnan')) #TypeError -->  never evr use Builtin functions as Identifiers


















