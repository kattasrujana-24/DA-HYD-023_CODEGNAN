'''
OOP --> Object Oriented Programming --> It is a mechanism or process which revolves around creating objects.
It consists of two imp properties:
Attributes: Attributes are variables which carry data to the class
Mehtods: A method is a function defined inside a class which carry the behaviour of the object.
Example chair(object): Wood, Tools, Dimenions(blueprint), Carpenter
Features of OOP --> Modularity, Scalability,
Encapsulation(binding the data(attributes),
Features to the class) (objects)
Abstraction --> shows only relevant information to the class(objects)
Inheritance --> Acquiring properties (attributes,methods)
Single -->Fngerprint
Multiple --> Parents (Mother,Father) -->Child
Multilevel --> GrandParent --> Parent --> Child
Polymorphism --> Method Overloading, Method Overriding, Operator Overriding
'''
#Syntax for clas creation:
'''
'''
class Class_Name:
    """Doc String"""
    attributes (characteristics)
    .......
    def func(self): (behaviour)
        ....
        .....
    .....
obj = Class_Name()
'''
'''
#Student Class with basic details
class Student:
    """Understanding the usage of OOP"""
    name = "Srujana"
    id = "CGH4085"
    gender = "female"
    email_id = "kattasrujana569@gmail.com"
    #Methods(behaviour)
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student ID is {self.id}')
        print(f'Student Mail is {self.email_id}')
u1 = Student()
print(u1)
#print(dir(u1) #directory (returns all available methods/attributes)
print(u1.display())
u2 = Student()
u2.display()
'''
'''
#Student Class for multiple objects
class Students:
    """Understanding the usage of OOP"""
    name = input("Enter the name:")
    id = input("Enter the ID No:")
    gender = input("Enter the Gender:")
    email_id = input("Enter the Mail id:")
    #Methods(behaviour)
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student ID is {self.id}')
        print(f'Student Mail is {self.email_id}')
'''        
u1 = Students()
u1.display()
u2 = Students()
u2.display()
print(u1.__dict__)
print(u2.__dict__)

'''
#Student Class for multiple objects
class Students:
    """Understanding the usage of OOP"""
    name = input("Enter the name:")
    id = input("Enter the ID No:")
    gender = input("Enter the Gender:")
    email_id = input("Enter the Mail id:")
    #Methods(behaviour)
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student ID is {self.id}')
        print(f'Student Mail is {self.email_id}')



#Create a class with Car Brand name,price,color --> dislay()







    
