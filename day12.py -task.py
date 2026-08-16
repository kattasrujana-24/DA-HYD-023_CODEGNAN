'''
#Student Marks Manager
marks = []
'''
#Requirement 1 & 2: Accept three marks and add them using append()
for i in range(3):
    marks = int(input("Enter a mark:"))
    marks.append(mark)
print("Original marks:",marks)

#Requirement 3: Insert 90 at the beginning
marks.insert(0,90)
print(marks)

#Requirement 4: Add 75 and 85 using
extend()
marks.extend([75,85])
print(marks)

#Requirement 5: Check for 75 and remove it
if 75 in marks:
    marks.remove(75)
    print("Removed final mark:",removed_mark)

#Requirement 6: Display final list and its length
print("Final list:",marks)
print("Length:",len(marks))

print("I have done")


#Number List Analyser
numbers = [20,10,30,20,40,20]
numbers.sort()
print("Ascending order:",numbers)
numbers.reverse()
print("Descending order:",numbers)
search_number = int(input("Enter a number to search for:"))
if search.number in numbers:
    print("Number found!")
    print("count:",numbers.count(search.number))
    numbers.count(search_number)
else:
    print("Number not found")
print("Smallest value:",min(number))
print("Total:", sum(numbers))


#Even and Odd Number Separator

numbers = [10,15,20,25,30,35]
even = []
odd = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print("Even numbers:",even)
print("Odd numbers:",odd)
print("First three values:",numbers[:3])
print("Last three values:",numbers[-3:])
backup = numbers.copy()
numbers.clear()
print("Original list after clear():",numbers)
print("Backup list:",backup)


#Unique Name Manager

name = ["Asha","Rahul","Asha","John","Rahul"]
unique_names = set(names)
unique_names.add("Meera")
unique_names.update(["Arun","Priya"])
if "John" in unique_names:
    unique_names.remove("John")
unique_names.discard("David")
print("Unique student names:")

for name in unique_names:
    print(name)

#Course student Comparision
    
python_students = {"Asha","Rahul","John","Meera"}
da_students = {"Rahul","Meera","Arun"}
print("Union:",
python_students.union(da_students))
print("Intersection:",
python_students.intersection(da_students))
print("Only Python:",
python_students.difference(da_students))
print("Only ine course:",
python_Students.symmetric_difference(da_students))

print("DA subject of python:",
da_students.issubset(python_students))
print("Python supersetof DA:",
python_students.issuperset(da_students))
print("Both are disjoint:",
python_students.isdisjoint(da_students))

print("Union students:")
for i in python_students.union(da_students):
    print(i)

print("Common students:")
for i in python_students.intersection(da_students):
    print(i)










