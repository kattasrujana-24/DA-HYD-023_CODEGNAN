'''
OOP-->Object Oriented Programming-->objects
An OOP is a mechanism or a process which revolves around creating objects it consists of two important properties
-->Attributes-->are variables which carry data to the class
-->Methods-->A method is a funtion defined inside a class which carry the behaviour of the object 
EX-->chair(object)-->wood,Tools,Dimensions(blueprint),carpenter
Features of OOP-->Modularity,Scalability,Encapusalation(binding the data(attributes),features to the class)(objects)
Abstraction-->show only relevant infprmation to the class(object)
Inheritance-->Acquring properties(attributes,methods)
Single-->Fingerprint
Multiple-->Parents(Mother,Father)-->child
Multilevel-->Grandparent-->parent-->child
Polymorphism-->Method Overloading,Method Overriding,Operator Overriding
'''
#syntax for class creation:
'''
class Class_Name:
    """Doc String"""
    attributes(characteristics)
    ..........
    def func(self):
        ......
        .......
    ........
obj=Class_Name()

#Student Class with basic details
class Student:
    """Understanding the usage of OOP"""
    name="Rashmitha"
    id="CGH3830"
    gender="Female"
    email_id="rashmithakatakam.13@gmail.com"
    #Methods(behaviour)
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student Id is {self.id}')
        print(f'student  Mail id is {self.email_id}')
u1=Student()
#print(dir(u1))#dictionay (returns all available methods/attributes )
print(u1.display())
u2=student()
print(u2.display())       

#student class for multiple objects
class Student:
    """Understanding the usage of OOP"""
    name=input("Enter the name:")
    id=input("Enter the id:")
    gender=input("Enter the gender:")
    email_id=input("Enter the Mail id:")
    #Methods(behaviour)
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student Id is {self.id}')
        print(f'student  Mail id is {self.email_id}')
u1=Student()
u1.display()
u2=Student()
u2.display()
print(u1._dict_)
print(u2._dict_)

#Student details with multiple objects
class Students:
    """Understanding the usage of OOP"""
    def data(self,name,id,gender,email_id):
        self.name=name 
        self.id=id
        self.gender=gender
        self.email_id=email_id
    #Methods(behaviour)
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student Id is {self.id}')
        print(f'Student  Mail id is {self.email_id}')
u1=Students()
u1.data("rashmitha","CGH3830","female","rashmithakatakam.13@gmail.com")
u1.display() 
print(u1._dict_)
u2.Students()
u2.data("Akash","CGH3456","Male","akash@gmail.com")
u2.display()
print(u2._dict_)
'''
#create a class with car brand name,price,color-->display()
class Cars:
    """Understanding the usage of OOP"""
    def car_data(self,brand,name,price,color):
        self.brand=brand
        self.name=name 
        self.price=price
        self.color=color
    #Methods(behaviour)
    def details(self):
        print(f'Car brand is {self.brand}')
        print(f'Car Model name is{self.name}')
        print(f'Car price is {self.price}')
        print(f'Car color is {self.color}')
u1=Cars()
u1.car_data("BMW","Sendas",color="White",price="50lakhs")
u1.details()
u2=Cars()
u2.car_data("MaruthiSuzuki","Swift",color="Blue",price="8lakhs")
u2.details()
