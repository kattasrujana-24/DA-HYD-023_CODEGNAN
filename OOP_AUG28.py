'''
OOP-->class(attributes,methods,constructor,instances methods)
object creation/utilisation -->Encapsulation,Inheritace,polymorphism
OOP -->Abstraction,Usage of class methods,static method

#Class methods -->these are termed by using @classmethod decorator
It applie for entire class level data,thereby every object utlisation will be modified..

#lets work on an exmaple related to Ecommerce

class Ecommerce:
    """" Usage of class method and class attribute"""
    company="Flipkart" #class attribute
    delivery_charge=50 #class attribute
    @classmethod
    def update_delivery(cls):
        cls.delivery_charge=100
        print(f'New delivery charges {cls.delivery_charge}')
product=Ecommerce()
print(product.company)
print(product.delivery_charge)
print(Ecommerce.company)
print(Ecommerce.delivery_charge)
product.update_delivery()
print(product.delivery_charge)
Mobile=Ecommerce()
print(Mobile.delivery_charge)
p=Ecommerce()
print(p.delivery_charge)
print(p.update_delivery)

#Applying Iheritance and usage class method

class RBI:
    """Inheritance usage and class method"""
    available_cash=500000 #class attribute
    @classmethod
    def rbi_cash(cls):
        print(f'Availble cash with RBI is{cls.available_cash}')
class SBI(RBI):
        pass
class HDFC(RBI):
    """Now we will also add some cash to it"""
    cash=300000
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is{cls.cash}')
        print(f'total cash is {HDFC.cash+RBI.available_cash}')
#a=SBI()
#print(a.available_cash)
#a.rbi_cash()
#SBI.rbi_cash() #we can aslo acess with classname directly
b=HDFC()
print(b.available_cash)
print(b.cash)
b.rbi_cash()
b.hdfc_cash()


class RBI:
    """Inheritance usage and class method"""
    cash=500000 #class attribute
    @classmethod
    def rbi_cash(cls):
        #print(f'Availble cash with RBI is{cls.cash}')
         print(f'Availble cash with RBI is{RBI.cash}')
class SBI(RBI):
        pass
class HDFC(RBI):
    """Now we will also add some cash to it"""
    cash=300000
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is{cls.cash}')
        print(f'Total cash is{HDFC.cash+RBI.cash}')


a=HDFC()
print(a.cash)
a.hdfc_cash()
a.rbi_cash()
a.hdfc_cash()
#If increse as above scenario we have same name for class attributes in 
#both parent and child classes,the best approach is to call
#the class attributes is using class names such as(RBI.cash)

#Static Method -->It does not depend either on the object or the class
#we can create it using@staticmethod decorator
#it is mainly used as utility or helper functions

class Ecommerce:
    """Usage of Static Method"""
    @staticmethod
    def free_delivery(price):
        return price>500
u1=Ecommerce()
print(u1.free_delivery(489))
print(u1.free_delivery(600))

# Now lets relate both class method and static method in a single use
class Ecommerce:
    """Usage of class &sttatic method"""
    platform ="flipkart" #classattribute
    @classmethod
    def show_platform(cls):
        print("Welcome to the platform:")
        print(f'{cls.platform}')
    @staticmethod
    def free_delivery(price):
            return price>500
            if  price>500:
                print("You rae eligible for free delivery")
            else:
                print("your need to pay delivery charges")
user=Ecommerce()
user.show_platform()
print(user.free_delivery(450))
print(user.free_delivery(1200))
'''
#Abstraction :it is aslo one of the key feature of OOp ,where it shows
#only the relevant details to the user and hidee the implemenataion
#Instagram -->Uploading photo ,Upload video,Reel
#we have abc module to implement abstraction
import abc
from abc import ABC,abstractmethod
class Content(ABC):
    @abstractmethod
    def upload(self):
        pass
class Photo(Content):
    '''def upload(self):
        print("Compressing the picture")
        print("Edit the picture")
        print("Photo uploaded sucessfully")'''
    pass #we made upload as abstract method mandatory it has be followed
class Video(Content):
    def upload(self):
        print("Encoding the video")
        print("Video Editing is in process")
        print("Video Uploaded Successsfully")
class Reel(Content):
    def upload(self):
        print("Adding Effects to the Reel")
        print("Reel is  Edited")
        print("Reel is Uploaded sucessfully with tags..")
'''Contents=[Photo(),Video(),Reel()]
#print(Contents)
for content in Contents:
    content.upload()'''
#obj=Photo()
#print(obj) #TypeError
a=Video()
print(a.upload())