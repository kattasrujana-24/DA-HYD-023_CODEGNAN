'''
File Handling in python: Files are mainly used to store the data
It supports --> r,w,a (read,write,append) using open() 

#First lets understand how we can access .txt files using Python

import os
if os.path.exists('sample.txt'):
    file = open('sample.txt','r')
    print("File is loaded Successfully")
else:
    print("File not present")

#Now let us access the content fromt the file
file = open('sample.txt','r')
#print(file)
#print(file.read()) #reads the entire content from the file
#print(type(file.read()))
#print(len(file.read()))
#a = file.read()
#print(a)
#print(len(a)) #assign to a varible and check the length amd apply desried funciton
#readline(),readlines()
#print(file)
#print(file.readline()) #reads single line from the file
#print(file.readlines()) #reads all lines from the file in a list


#'w' mode --> It automatically creates a new file,if the file exists it overrides the content in it

file = open('data.txt','w')
print(file)
#as the file is automatically create lets write content to it
file.write("Good Afternoon everyone,how are you doing?")
file.write("Today is wednesaday...")
file.close()

#we can also use with keyword to avoid close()
with open('data.txt','w')as f:
    f.write("Now checking what happened")

#'a' --> It also automtatically creates a file, but if the file is already existing it appends the content to the previous file

with open('data.txt','a') as g:
    g.write('\n okay let us see how its going')

#+ --> read and write 
with open('data.txt','r+') as h:
    print(h.read())
    #h.write("Today is wednesday")
#In the above case we can perform both read and write operations

#File operations size and path
import os
file = open('data.txt','r')
if os.path.exists('data.txt'):
    print("File size is",os.path.getsize('data.txt'),"Bytes")
    print("File Absolute path is",os.path.abspath('data.txt'))
else:
    print("File is not present")
'''

#If your project is requiring File Handling uses it...
#Tokens --> Operators --. Control  Statement(for,while,if,else,elif,break,continue)
#POP (FUnctios(*args/**kwargs)) --> OOP
#Data Analysis --> Numpy,Pandas,Data Visualization

    

