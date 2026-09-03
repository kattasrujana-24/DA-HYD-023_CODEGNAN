'''
OOP-->Class,Object,Methods(__init__())
Encapusaltion-->Public,Private,Proected
Inheritance--> It is one of the key feature of OOP where we inherit the properties (attributes/methods)from one class to another
class(base class(parent class)-->derived class(child class))
whatsapp-->Personal,User,Business User(Catalog),Community 
Features--> Code Reuseability,Avoiding code Duplication,Code Maintainability,Polymorphism(Method overriding(super()),
Method Overloading,Operator Overloading __add__,__str__)
Types: Single Inheritance(Finger Print)
-->One child class Inheriting Properties from one parent class Multiple Inheritance(Mother,Father-->child)-->one child
class inheriting properties from two parent classes
Multilevel Inhertance(GrandParent-->parent-->child)
level  by level
Hierarchical Inheritance-->multiple child classes inherting properties from single parent
Hybrid Inheritance-->OIt can carry one or more type of inheritances
Syntax:

single Inheritance:

class baseclass:
    statement(s)...
    .....
class Derivedclass(baseclass)
    ......
    ......

#Whatsapp Scenario-->personal User,Business User

class User:
    """Single Inheritance usage"""
    def send_msg(self):
        print('Sending msg')
    def voice_call (Self):
        print('Making voice calls')
    def video_call(self):
        print('Making video calls')
class BusinessUser(User):
    #pass
    def create_catalog(self):
        print("Displaying Products catalog")        
u1=BusinessUser()
print(dir(u1))
u1.send_msg()
u1.voice_call()
u1.video_call() 
u1.create_catalog()                  


#Social Media Login-->users-->update_users
class Users:
    """Single Inheritance usage"""
    company="codegnan"#class attribute
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def full_name(self):
        return self.fname + self.lname
#u1 = Users("rashmitha","katakam")
#print(u1.full_name())
#print(u1.company) 
class update_users(Users):
    def update_name(self):
        return self.fname.title()+" "+self.lname.title().strip()
u1=update_users("rashmitha" , "katakam")
print(u1.company) 
print(u1.full_name())
print(u1.update_name())  
u2=Users("sai","tarigopula")
print(u2.full_name())
print(u2.company) 

#What is we have constructor in child class also...
# Father-->Kid (property)

class Father:
    """Usage of Constructor in Single Inheritance""" 
    def __init__(self):
        self.property = 100000
    def father_property(self):
        print(f'Father property is{self.property}')
#class Kid(Father):
    #pass
class Kid(Father):
    """Now child class will have Constructor"""
    def __init__(self):
        #self.property = 200000
        self.cash = 200000
    def Kid_property(self):
        print(f'kid property is{self.property}')        
obj=Kid()
obj.father_property() 
obj.Kid_property()  
#in above case giving same value for father also as
# 2lakhs..when we gave property as same attribute in both class
# in this example parent class is having constructor and child class having constructor so,constructor overriding is happening
# to avoid construct overriding we start using super() method
# three types
# -->super().__init__()
# -->super().__init__(args)
# super().method()
'''
#in above class we use super().__init__()
class Father:
    """Usage of Constructor in Single Inheritance""" 
    def __init__(self):
        self.property = 100000
    def father_property(self):
        print(f'Father property is{self.property}')
#class Kid(Father):
    #pass
class Kid(Father):
    """Now child class will have Constructor"""
    def __init__(self):
        super().__init__()#calling superclass constructor
        #self.property = 200000
        self.cash = 20000
    def Kid_property(self):
        print(f'kid property is{self.cash}') 
        print(f'kid Final propery is {self.cash + self.property}')       
obj=Kid()
obj.father_property() 
obj.Kid_property()