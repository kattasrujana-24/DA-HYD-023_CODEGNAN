'''
Sequences -->Strings,Lists,Set,Frozenset
Mapping -->Dictionary
'''
'''
#Sets -->A set is a unique collection of objects,unordered,mutable,hashing
#Hashing,Unindexed,Unique,Heterogenous
#set(),{}
#a = {} its an empty dictionary
a = set()
print(type(a))
stud_ids = {123,345,234,564,234}
print(stud_ids)
print(type(stud_ids))
print(len(stud_ids))
#print(stud_ids[2])#TypeError

print(234 in stud_ids)
print(stud_ids*2)#set cant be repeated
print(stud_ids + stud_ids)#two sets cannot be merged

data = {12,3,4,5,[12,3,4],'saketh'}
print(data)
#No lists inside a set(hashing technique)Lists are Mutable

data = {12,3,4,5,(12,3,4),'saketh'}
print(data)
print(len(data))
for i in data:
    print(i)

#Methods on sets -->add(),update(),remove(),discard(),pop()
'''
names = {'srujana','shiva','chinnu'}
'''
print(len(names))
#add() will insert an element into the set(it can be anywhere but only unique)
names.add('python')
#print(names)
#names.add('srujana','chinnu')
#print(names)
names.add(('pol','pollice'))
print(names)'
'''
da_names = {'mani','shiva','chinnu','sujju'}
'''
#update()we can update multiple elements (set)

names.update(da_names)
print(names)
print(len(names))
print(da_names)
print(len(da_names))
da_names.update(names)
print(len(names))
print(len(da_names))

#remove(),discard(),pop(),clear()
#remove()removes an element from the set(it must be a number)
da_names.remove('shiva')
print(da_names)
#discard()will remove an element if its present else ignores
da_names.discard('codegnan')

da_names.pop()
print(da_names)
print(da_names.pop())#removes and returns an arbitary element
print(da_names)
da_names.clear()
print(da_names)
da_names.add('saira')
print(da_names)
da_names.update(['shiva','chinnu'])
print(da_names)

#copy()#creates a shallow copy of set(independent of each other)
d = da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)
print(da_names)
'''

#mathematical operations --> union(),intersection(),difference(),symmetric_difference
#issubset(),issuperset(),isdisjoint()

da_23 = {12,23,34,45,23,36}
da_24 = {34,46,47,23}
#event = da_23.union(da_24)
'''

event = da_23|da_24 #union()
print(event)
print(len(event))
#common = da_23.intersection(da_24)
common = da_23&da_24 #& intersection()
print(common)
#print(len(common))
common = da_23,intersection_update(da_24)
print(common) #returns none
print(da_23)#common elements are finally stored

print(da_23)
print(da_24)
#difference() removes common elements and prints remaining elements form first and second
#diff = da_23.difference(da_24)
#print(diff)
#f = da_23-da_24
#print(f)
#symmetric_difference() -->removes common elements and prints all rmng
#elements from two sets
symm = da_23.symmetric_difference(da_24)
#print(symm)
h = da_23^da_24
#print(h)


#issubset() -->checks for all elements to be present in other sets
da_24.remove(46)
da_24.remove(47)

print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))

#isdisjoint()returns false for sets having common elements
print(da_23.isdisjoint(da_24))
'''
#length of unique student ids in a class,where user can enter first input
#he should be giving number of student_ids,he will enter student_ids

a = int(input())
student_ids = input().split()
print(student_ids)
result = set(student_ids)
print(len(result))









