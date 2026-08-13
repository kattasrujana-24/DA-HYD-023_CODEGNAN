'''

Lists,Tuples...

#List --> Mutable,Ordered,Heterogenous
#index(),count(),copy(),sort(),reverse()

details = ['codegnan',7,2018,'Hyderabad']
print(len(details))
print(details.index(7))
print(details.index('codegnan'))
details.extend([7,21,45,21])
print(details.index(21)) #it returns first occurance
print(details.index(21,6))
#print(details.index('python')) #valueError

print(details.count(21))
print(details.count('python'))
'''
'''
data = ['codegnan','saketh','python','java'] #input
#output

0 : codegnan
1 : saketh
2 : python
3 : java

for obj in data:
    print(data.index(obj),':',obj)
#or
for obj in range(len(data)):
    print(obj,':',data[obj])
 
#copy() -->shallow copy of the given collection

new = data.copy()
print(new)
print(type(new))
print(len(data))

new[2] = 'Agentic AI'
print(new)
print(data)

data.append('srujana')
print(new)
print(data)

data.extend('srujana')
print(new)
print(data)

print(data.pop())
print(new)
print(data)

data = [1,2,3,[23,34,45],9,]
print(data)
new = data.copy()
print(new)

new[3][2] = 'Agents' #whenever we make changes in nested list original will also be effected
print(new)
print(data)

new[1] = 'python'
print(new)
print(data)
'''
'''
marks = [12,23,-45,76,56]
print(marks)
#print(marks.sort()) #returns None
#print(marks) #returns in ascending order
marks.sort(reverse = True) #returns in Descending order...
print(marks)
marks.insert(3,'code')
#marks.sort()
#reverse() -->returns in reverse order
marks.reverse()
print(marks)
print(marks[::-1])#reverse order


#type(),len(),max(),min(),print()

print(sorted('codegnan'))
#print(sorted(['code',12,23,76])) #raises Error
'''
'''
#Tuples -->Tuples are Indexed,Ordered,Heterogenous,Immutable collection
#dimensions,coordinates,database records,we prefer () for tuple notation
a = ()
print(type(a))
print(len(a))

dimensions = 1.5,2.5
print(dimensions)
print(type(dimensions))
print(len(dimensions))

#Operations -->Indexing,Slicing,Striding,Membership,Merging,Repetition
'''
courses = ('PFS','JFS',('DA','DS'),'AgenticAI',[100,6,6])
'''
print(courses)
print(len(courses))
print(courses[-1][2])
print(courses[-2][3])
print(courses[3][-2:])
#courses[2] = 23 Tuples are immutable
courses[-1].append('codegnan') #we can make any modifications inside list
print(courses)

#Create a Nested tuple as above and work on Slicing,Striding and List Functions

print('PFS' in courses) #Membership
d = courses * 2
print(d)
e = courses + (2,3,4,5) #merging
print(e)
'''
'''
#Tuples Immutable -->count(),index()
print(courses.index('AgenticAI')) #returns first occurance
print(courses.count('Agents'))      

#print(courses.sort()) #AttributeError -->sort() is in Lists not in Tuples

print(sorted(courses[-1]))
#print(sorted(courses)) #as we have mixed type

#TypeCasting
d = tuple(sorted((23,12,3,4,5))) #Ascending Order
print(d)
'''
'''
#accept group of integers space separated
a,b = map(int,input("Enter the values:").split())
print(a,b)

a = tuple(map(int,input("Enter the values:").split(',')))
print(a,)

'''
print('9+4')
#eval() function can take any kind of input
print(eval('9+4'))

a = eval(input("Enter a List:")) #in this case you can exactly enter data as list
print(a)
print(type(a))
#




















