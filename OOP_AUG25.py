'''class Father:
    """Usage of Constructor in Single Inheritance""" 
    def __init__(self):
        self.property = property
    def father_property(self):
        print(f'Father property is{self.property}')
#class Kid(Father):
    #pass
class Kid(Father):
    """Now child class will have Constructor"""
    def __init__(self,cash,property):
        self.cash = cash
        super().__init__ (property)
    def Kid_property(self):
        print(f'kid property is{self.cash}') 
        print(f'kid Final property is {self.cash + self.property}')       
obj=Kid(250000,1000000) 
obj.Kid_property() 
obj.father_property()
'''
#what child clss is having same method name as 
# parent class --> Method Overriding
# Area ofsquare/rectangle
'''
class Rectangle:
    """Method Overriding usage"""
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        print(f'Area of Rectangle is {self.x *self.y}')
class Square(Rectangle):
    def __init__(self,x):
        self.x=x
    def area(self):
        print(f'Area of Square is {self.x**2}')
class Rectangle(Square):
    def __init__(self,x,y):
        self.y=y
        super().__init__(x)
    def area(self):
        super().area() #calling sperclass method
        print(f'Area of Rectangle is {self.x*self.y}')
x,y=map(int,input("Enter the values:").split(','))
obj=Rectangle(x,y)
obj.area()
'''
#Multiple Inheritance
'''
class Parent1:
    ........
class Parent2:
    ........
class Child(Parent1,Parent2):
    .....
'''
class User:
    """Fisrt Parent class with User features"""
    def voice_call(self):
        print('Making Voice Calls')
class Notifications:
    def notification(self):
        print("Sending Notifications..")
class PremiumUser (User,Notifications):
    def verification_badge(self):
        print("Blue Tick Verification done")
user=PremiumUser()
user.verification_badge()



