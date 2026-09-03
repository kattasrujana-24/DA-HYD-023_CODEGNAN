'''
Polymorphism --> It is also one of the key feature of OOP
Poly --> many
Morph --> forms
Methods wuth same name can take different parameters (arguments--> lists,...)
-->Mehtod Overloading (compile time polymorphism)
-->Method Overriding (Reun-time)
-->Operator Overloadinf (+,*) (__add__,__str__)

HotStar
->Free User -->can watch the movies with advertisements
->Premium USer -->can watch premium content with advertisements
->VIP User -->live content,streaming quality,premium content

#Method Overloading:

class HotStar:
    """Understand Polymorphism"""
    def watch():
        print(f'User logged into HotStar...Opening home page')
        def watch(self,movie):
            self.movie = movie
            print(f'User watching {self.movie}')
app = Hotstar()
app.watch("Leo")
#app.watch() it returns error as watch()  is overloaded
'''

#1)Method usage default arguments
#2)Method usage with vaiable length arguments(*args) 
#3)Method usage wtih type of arguments
'''
class HotStar:
    """Method usage with default arguments"""
    def watch(self,movie=None):
        if movie is None:
            print(f'User logged into HotStar..checking..')
        else:
            self.movie=movie
            print(f'User started watching {self.movie}')
app =HotStar()
app.watch()
app.watch("Vikram")
'''
'''
class Hotstar:
    """Method usage with variable length arguments"""
    def add_watchlist(self,*movies):
        print(movies)
        for movie in movies:
            self.movie = movie
            print(f'User started watching {self.movie}')
app =Hotstar()
app.add_watchlist()
app.add_watchlist("salaar","vikram","varsham")

#method overloading with type of arguments usage
#Hotstar --> one movie at a time
         --> multiple movies at a time
'''
'''
class Hotstar:
    """Method overloading with type of arguments usage"""
    def watch(self,content):
        if isinstance(content,str):
            print(f'User watching {content}')
        elif isinstance (content,list):
            print(content)
            for movie in content:
                print(movie)
app=Hotstar()
app.watch("sap")
app.watch(["salaar","darling","billa"])

#method overriding --> It happens in the scenario of Inheritance, where if child class is having name same as parent class
#that's where overriding occurs
#we can use super() or if we create different objects
'''
'''
class Freeuser:
    """Understanding method overriding"""
    def watch(self):
        print("User logged into Homepage...")
class PremiumUser(Freeuser):
    """Using Inheritance"""
    def watch(self,movie):
        super().watch() #calling superclass method
        self.movie=movie
        print(f'User watching {self.movie}')
obj = PremiumUser()
obj.watch("vikram")
obj2 = Freeuser()
obj2.watch()
'''
'''
#Operator Overloading --> Operators (+,-,*,/) --> Operators will behave in a different wat as per user defined objects...

# + (Addition,Concatenation,Merging)

print (3+4) #Addition
print('code'+'gnan') #Concatenation
print([23,45]+[4,5]) #Merging

#print(3.__add__(4)) #__add__(self,other)
a =25;b=3
print(a.__add__(b))
a = [12,3,4];b = [3,4,5]
print(a.__add__(b)) #Merging
print(a.__len__()) #len(a)
print(a.__mul__(2)) #print([12,3,4]*2)
'''
'''
#let's apply the above scenario HotStar WatchHistory

class WatchHistory:
    """Define the number of hours"""
    def __init__(self,hours):
        self.hours = hours
varun = WatchHistory(100)
print(varun.hours)
akash = WatchHistory(120)
print(akash.hours)
#print(varun + akash) #TypeError unsupported operation
print(varun.hours + akash.hours)


#But the preferable way is usage of __add__()
class WatchHistory:
    """Define the number of hours"""
    def __init__(self,hours):
        self.hours = hours
    def __add__(self,other):
        return self.hours + other.hours
    def __str__(self):
        return f'WatchHistory is  {self.hours}'
varun = WatchHistory(300)
print(varun) #__str__() method
akash = WatchHistory(50)
print(akash)
print(varun + akash)

1.
# Defining the entities as standalone classes
class University:

    def __init__(self, name):
        self.name = name


class Course:

    def __init__(self, code, name, schedule):
        self.code = code
        self.name = name
        self.schedule = schedule


class Faculty:

    def __init__(self, name, faculty_id):
        self.name = name
        self.faculty_id = faculty_id


class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


# Creating individual object instances of the classes
uni = University("Global Tech University")
course1 = Course("CS101", "Python OOP", "Mon 10:00 AM")
faculty1 = Faculty("Smith", "FAC-01")
student1 = Student("Sharma", "STU-101")

print(f"University: {uni.name}")
print(f"Course: {course1.name} ({course1.code})")
print(f"Faculty: {faculty1.name}")
print(f"Student: {student1.name}")


# Hierarchy 1: Department inherits from University
class University:

    def __init__(self, name):
        self.name = name


class Department(University):

    def __init__(self, uni_name, dept_name):
        super().__init__(uni_name)
        self.dept_name = dept_name


# Hierarchy 2: UndergraduateStudent inherits from Student
class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class UndergraduateStudent(Student):

    def __init__(self, name, student_id, max_credits=18):
        super().__init__(name, student_id)
        self.max_credits = max_credits

dept = Department("Global Tech University", "Computer Science")
ug_student = UndergraduateStudent("Rahul", "UG-101")
print(f"{ug_student.name} is in {dept.dept_name} at {dept.name}")

class Student:

    def __init__(self, name):
        self.name = name
        self.courses = []

    def enroll(self, course_name):
        self.courses.append(course_name)

    def view_schedule(self):
        print(f"Schedule for {self.name}: {self.courses}")


class UndergraduateStudent(Student):

    def enroll(self, course_name):
        # Undergrad specific enrollment rule
        print(f"[UG Enrollment] Checking prerequisites for {self.name}...")
        super().enroll(course_name)

    def view_schedule(self):
        print(f"[UG Schedule] {self.name}'s Classes: {', '.join(self.courses)}")


class GraduateStudent(Student):

    def enroll(self, course_name):
        # Graduate specific enrollment rule
        print(f"[Grad Enrollment] Verifying advisor approval for {self.name}...")
        super().enroll(course_name)

    def view_schedule(self):
        print(
            f"[Grad Research/Class Schedule] {self.name}'s Advanced Courses: {', '.join(self.courses)}"
        )


# Same method calls behave differently
students = [
    UndergraduateStudent("Rahul"),
    GraduateStudent("Ananya"),
]

for s in students:
    s.enroll("CS101")
    s.view_schedule()

class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.__student_id = student_id  # Private attribute
        self.__grades = {}  # Private attribute

    # Public Getter for ID
    def get_student_id(self):
        return self.__student_id

    # Public Setter/Method for Grades
    def add_grade(self, course_name, grade):
        self.__grades[course_name] = grade

    # Public Getter for Grades
    def get_grades(self):
        return self.__grades


student = Student("Rahul", "STU-999")
student.add_grade("Python", "A")

print(f"ID: {student.get_student_id()}")
print(f"Grades: {student.get_grades()}")
# student.__grades will raise an AttributeError

class Course:

    def __init__(self, course_name):
        self.course_name = course_name
        self.roster = []

    def add_student(self, student_name):
        self.roster.append(student_name)


class Faculty:

    def __init__(self, name):
        self.name = name

    # Abstracting internal list formatting behind a simple method call
    def view_roster(self, course):
        print(f"\n--- {course.course_name} Roster (Instructor: {self.name}) ---")
        for idx, student in enumerate(course.roster, start=1):
            print(f"{idx}. {student}")


prof = Faculty("Dr. Alan")
course = Course("CS101 - Intro to Python")
course.add_student("Rahul")
course.add_student("Ananya")
prof.view_roster(course)
'''
2.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Manager inherits from Employee
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

# Developer inherits from Employee
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

# Example usage
mgr = Manager("Alice", 90000, "IT")
dev = Developer("Bob", 80000, "Python")
print(mgr.name, mgr.department)
print(dev.name, dev.programming_language)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    # Overriding details()
    def details(self):
        return f"Manager: {self.name}, Department: {self.department}, Salary: ${self.salary}"

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    # Overriding details()
    def details(self):
        return f"Developer: {self.name}, Tech: {self.programming_language}, Salary: ${self.salary}"

# Example usage
team = [Manager("Alice", 90000, "IT"), Developer("Bob", 80000, "Python")]
for member in team:
    print(member.details())

class Employee:
    total_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1

    @staticmethod
    def get_employee_count():
        return Employee.total_employees

# Example usage (can be called without creating an instance)
print("Initial Count:", Employee.get_employee_count())

emp1 = Employee("Alice")
emp2 = Employee("Bob")

print("Updated Count:", Employee.get_employee_count())

class Employee:
    total_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1

    @classmethod
    def get_employee_count_classmethod(cls):
        return cls.total_employees

# Example usage (accesses class variables via 'cls')
emp1 = Employee("Alice")
emp2 = Employee("Bob")

print("Total Employees via classmethod:", Employee.get_employee_count_classmethod())

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Overload print()
    def __str__(self):
        return f"Employee(Name: {self.name}, Salary: ${self.salary})"

    # Overload ==
    def __eq__(self, other):
        return self.salary == other.salary

    # Overload <
    def __lt__(self, other):
        return self.salary < other.salary

    # Overload >
    def __gt__(self, other):
        return self.salary > other.salary

# Example usage
emp1 = Employee("Alice", 70000)
emp2 = Employee("Bob", 85000)
emp3 = Employee("Charlie", 70000)

print(emp1)            # Triggers __str__
print(emp1 == emp3)    # Triggers __eq__ -> True
print(emp1 < emp2)     # Triggers __lt__ -> True
print(emp2 > emp1)     # Triggers __gt__ -> True
