'''
Tokens -->Keywords,Identifiers,Literals,Operators,Punctuators,Variables
Operators -->Numeric data (int,float,complex),bool
Control Flow --> if,elif,else,for,while
Sequences -->strings,lists,sets,tuples,mapping(dict)
'''
#Strings -->Group of characters ,we use single or double or triple quotes
#for representation of strings...
#Strings are Immutable,Ordered,Indexed Collection
#space is also a character

name = 'Codegnan'
print(name)
print(type(name))
print(len(name)) #len -->returns the number of items in a container
'''
#index() --> fetch the object (position) starts at 0 and ends at len(object)
#we use [] representation
print(name[0])
#print(name[25]) #IndexError --> as it's out of range

#Negative Indexing --> -1 to len(obj))
print(name[-1]) #it returns the last character
print(name[-3])
#print(name[-23]) #indexerror

#Slicing -->we can access group of characters(objects)
#we use [start:end] #start default --> 0,start is included,end is excluded

print(name[:]) #returns the entire string
print(name[0:])#returns the entire string
print(name[:4])#starts at 0th index before 4th index
print(name[1:5])
print(name[5:])
print(name[6:])

name = 'python'
print(name[7:3])#returns empty as strings are immutable
#slicing is applicable from lower index to higher index
print(name[3:7])
print(name[:45])#returns till the end of the string
print(name[45:])

print(name[-1:-5])#returns empty string
print(name[-5:-1])#starts at -5 and ends at -2
#print 'on' from above string
print(name[4:])
print(name[-1:-3])
print(name[-2:])

print(name[1:-2])
print(name[2:-6])
#observe +ve,+ve, -ve,-ve & +ve,-ve all possibilities
'''
#Striding --> [start:end:step]
'''
course = 'DataAnalysis'
print(len(course))
#Data -->result
print(course[:4])
print(course[4:1])
print(course[-3:])

print(course[::1]) #returns all characters
print(course[::2]) #includes start to end skipping 1 character

print(course[1:6:3]) #[1:6] -->ataAn -->[1:6:3] --> aA

print(course[2::3])

print(course[::-1])
print(course[::-2])

#task -->workout with all possibilities of slicing and striding on a example

name = 'codegnan'
#name[3] = 'w' #strings are immutable

#Operations on Strings -->Indexing,Concatenation,Repetition
print(name * 3)
print('*' * 25)#repetition

#Concatenation --> combining strings

data = 'srujana' + 'python' + 'database'
print(data)
print('123' * 4) #Numeric String
print('code' in 'codegnan')

for i in 'codegnan':
    print(i,':')
#in above case we get every character line by line

for i in 'codegnan':
    print(i,end=' ')

name = "codegnan"
#Built-in functions --> len(),min(),max(),sorted()
print(len(name))
print(min(name)) #alphabetical order ASCII ordering
print(ord('A'))
print(ord('a'))
print(max(name))
print(chr(97))
print(sorted(name)) #returns a list by sorting all elements
'''

#Methods on Strings --> Case-Conversions,Finding/Searching...
name = 'Codegnan data'
#case-conversions -->upper(),lower(),title(),capitalize()
a = name.upper()
print(a)
b = name.lower()
print(b)

#Capitilize() --> converts first letter to uppercase
c = name.capitalize()
print(c)
d = name.title()
print(d)

#Task : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#use loops and strings to return A-Z







































