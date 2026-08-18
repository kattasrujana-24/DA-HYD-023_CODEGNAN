'''
Tokens,Datatypes -->Control Flow Statements -->if,elif,else,for,while,break,continue...

Procedure Oriented programming
Functions -->A function is a block of code which performs a specific task
Its a reusble group of statements where we define using def keyword
Advantages --> Code reusaility,code maintainability,ease of debuggin,avoiding code duplication,modularity

def fname(parameters) : Function defn
    """Doc String""" Description
    statements(s)...
    ..........            Function bofy
    return valuse(s)....
fname{args} Function call

#To Perform sum of given objects
a = {1,3}
b = {4,5}
print(a+b)
'''

'''def add(a,b):
    """Sum of objects"""
    c = a+b
    return c
print(add(12,3)) #Addition
print(add('code','gnan')) #Concatenation
print(add([12,5],[12,34])) #Merging     
c,d = map(int,input("Enter the values:").split(','))
print(c,d)
print(add(c,d))
'''
'''
def add(a,b):   
    """Sum of object without return"""
    print(a+b)
add('code','gnan')    
print(add(12,-34)) #it returns result along with None
'''
'''
#usage of return

name,age,salary = "saketh",32,50000

def details():
     #return name,age,salary
     #return "Codegnan"
     #return 23+34+45
      return #it returns None as output
print(details())    

There are 5 types of Arguments:

--> Positional Arguments
--> Default Arguments
--> Keyword Arguments
--> Variable length arguments (*args)
--> Keyword variable length arguments (**kwargs)
'''
'''
#Positional Arguments --> Number of arguments in function defn should match with function call(order has to maintained)
#print(len(123,234)) this is as per built-in len(obj) will accept one argument

def details(name,place):
    """To store the details"""
    #name = "Codegnan"
    #place = "Hyderabad"
    return name,place
    print(f'Name is {name}')
    print(f'Place is {place}')
#print(details("saketh","codegnan"))
#print(details("sai","vizag"))
#print(details("vizag","shyam",34)) #raises TypeError as only 2 arguments to be given
c,d = map(str,input("Enter the values").split(','))
details(c,d)
'''
'''
#Default arguments -->we can make arguments as default but not first argument as default
#def grocery(item,price=35):
#def grocery(item="Cheese",price=100):
def grocery(item="Burger",price) #non default always follows default     
    
    """usage of default arguments""" 
    print(f'The Item is {item} and price is {price}')

grocery("Milk",32)
#grocery(32,"Milk")
grocery("Bread") #by default we have given price as 35
#grocery("Bread",45)
grocery() #as both item and price as default arguments
'''

#keyword arguments --> Whenever we want to specify the name of argument
def employee(name,salary,role,place="Codegnan"):
    """Keyword arguments usage"""
    print(f'Employee name is {name},role is {role},salary is {salary},works in {place}')
employee("sai",20000,"Admin")
employee(salary=25000,role="Frontdesk",name="Asha")
employee("Asha",25000,"IT","Cognizant")









