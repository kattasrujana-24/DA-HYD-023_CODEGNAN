'''
Constructor-->Instance methods-->Public Attributes
Encapsulation
Constructor-->It is a special method (__init__())

class Cars:
    """Understanding the usage of Constructor in OOP"""
    def __init__(self,brand,name,price,color):
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
#u1=Cars("Tata","Nexon","9lakhs","Blue")
#u1.details()

class Cars:
    """Understanding the usage of OOP"""
    def __init__(self,brand,name,price,color):
        self.brand="BMW"
        self.name="Sedans"
        self.price="50lakhs"
        self.color="White"
    #Methods(behaviour)
    def details(self):
        print(f'Car brand is {self.brand}')
        print(f'Car name is{self.name}')
        print(f'Car price is {self.price}')
        print(f'Car color is {self.color}')
u1=Cars()
print(u1.brand,u1.name,u1.color,u1.price)
u1.details()

Encapsulation --> It is one of the main feature of OOP.
It binds (bundles)the data (attributes)and the methods(behviour)
into a single unit (class)-->Multiple objects
-->Attributes-->Public,Protected,Private
#Public attributes-->Attributes defined inside the class()
and can be modified outside the class

class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username):
        self.user=username #Public attribute
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
u1=CodegnanPortal("rashmitha")
u1.display()
print(u1.__dict__)#returns the key-value pairs for attribute
u2=CodegnanPortal("Navya")
u2.display()
print(u2.__dict__) 

#Protected Attributes--> we use single underscore before an
#attribute moreovern it can be modified also outside the class
#and even accessible in subclass....
 
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username,_otp):
        self.user=username #Public attribute
        self._otp=_otp #protected attribute
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
        print(f'student has received OTP as{self._otp}')
u1=CodegnanPortal("rashmitha",12345)
u1.display()
u1._otp=3456
u1.display()        

#Private Attributes -->we use special notation as double underscore
#such as __password
#Accessble only inside the class and cannot be directly
#modify
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username,_otp,password):
        self.user=username #Public attribute
        self._otp=_otp #protected attribute
        self.__password=password #private attribute
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
        print(f'student has received OTP as{self._otp}')
       #print(f'Student password is {self.__password}')
u1=CodegnanPortal("rashmitha",23456,"admin123")
#print(u1.password)attribute error  as password is private
print(u1.__dict__)
print(u1._CodegnanPortal__password)#NameMangling
'''
#In above case we are using Namemangling but he right way is 
#usage of getter() and setter() methods
        
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username,_otp,password):
        self.user=username #Public attribute
        self._otp=_otp #protected attribute
        self.__password=password #private attribute
    #usage of getter() method
    def get_password(self):
        #return "*****"
        return self.__password
    #to modify the password we use setter() method    
    def set_password(self,new_password):
        if len(new_password)<=6: 
            print("wrong password not satisfied 6 characters")
        else:
            self.__password = new_password
            print("Now password is updated") 
u1=CodegnanPortal("rashmitha",23456,"admin123")
print(u1.get_password()) #attribute error
u1.set_password("rashmitha")
print(u1.get_password())
u1.set_password("rashmi123")#compulsory more than 6
print(u1.get_password())

