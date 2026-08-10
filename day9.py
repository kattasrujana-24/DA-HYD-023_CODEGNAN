'''
Strings --> CaseConversions,Searching & Finding,String testing methods,
Replace,Space removal

#Searching,Finding,Replacing,Joining...
a = "Codegnan"
print(len(a))
print(min(a))
print(max(a))

b = a.index('g') #it returns the index position
print(b)
c = a.index('n') #it returns only the first occurance
print(c)
d = a.index('n',6)#it returns the next occurance
print(d)
#e = a.index('n',8) #value error
#print(e)
#f = a.index('t') #value error
#print(f)
g = a.index('n',2,6)
print(g)
'''
'''
#rindex() -->returns last occurance
b = a.rindex('g')
print(b)
c = a.rindex('n') #here 'n' is occuring at 7th index
print(c)
#d = a.rindex('n',8) #it reurns valueerror
#print(d)

#count() -->returns the number of items object is repeating
print('Codegnan'.count('n'))
print('Code'.count('w')) #it returns 0 as we dont have 'w' in 'Code'
print('Cakshjasaksajs'.count('a'))

#find()-->first occurance but it avoid error returns -1 if substring is not found
print('Codegnan'.find('r'))
print('Codegnan'.find('n'))
print('Codegnan'.rfind('n'))

a = "DataAnalysis"
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(1))

#Replacing,Splitting,Joining

#strings are immutable
a = 'Codegnan'
#a[4] = 's'
print(a.replace('g','s'))
print(a)
a = a.replace('g','s')
print(a)
print('fghijki#kajaksh#kfllfl'.replace('#',' '))
print(a.replace('x','saketh')) #empty

a = 'code srujana python'
b = a.split()#by default if we have space it splits(returns list)
print(b)
print(len(b))
c = 'code,srujana,python'
d = c.split()
print(d)
e = c.split(',')
print(e)
'''
'''
#join()
a = 'code'
b = 'gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('srujana'))
print(' '.join('srujana'))
'''
#String testing methods (boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower()...
'''
a = 'Codegnan123'
print(a.isalnum()) #returns True for alphanumeric strings else False
b = 'Codegnan'
print(b.isalnum())
print(a.isalpha()) #returns True only for alphabets
print(a.isdigit()) #returns True only for digit string
print('9248906269'.isdigit())
print('2345'.isnumeric()) #this has upper edge (numbers,fractions,romans)
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))

print('codegnan'.islower()) #returns True for all lowercase
print('codegnan'.isupper()) #returns False for all uppercase
print('Codegnan Python'.istitle())
'''
#Space removal --> strip() (removes leading and trailing spaces)
'''
a =' codegnan '
print(a.strip())
b = input("Enter the string:").strip().lower()
print(b)
'''
#zfill() filling with zeros as per the given numeric string
print('234'.zfill(4))
print('234'.zfill(7))

print('hai'.center(6))
print('hai'.center(6,'#'))

print('hai'.ljust(6,'#'))
print('hai'.rjust(6,"#"))






























