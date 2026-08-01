'''
task : Student marks and grade analyzer
90-100 --> 'A'
80-89 --> 'B'
70-79 --> 'C'
60-69 --> 'D'
<60 -->Fail
#also -ve cases should not be allowed and marks souldnt be greater than

marks = int(input("Enter the marks (1-100):"))
if marks > 0 and marks <=100:
    if marks >= 90:
        print("User has secured Grade A")
        
    if marks >= 80 and marks <=89:
        print("User has secured Grade B")
        
    if marks >= 70 and marks <=79:
        print("User has secured Grade C")
        
    if marks >= 60 and marks <=69:
        print("User has secured Grade D")
        
    if marks <60:
        print("User has failed,study again")
else:
    print("Enter only +ve values greater than 0 and less than 100")

#elif keyword --> if-elif-else

if <condition1>:
     statment(s)...
if <condition2>:
     statement(s)...
if  <condtion3>:
     statement(s)...
     .......
     ........
else:
    statement(s)...
    .......
   
marks = int(input("Enter the student marks:"))
if marks >=100:
    print("Entered vlues should be greater than 1 and less than 100")
elif marks >=90 and marks <=100:
    print("User has secured Grade A")
elif marks >=80 and marks <=89:
    print("User has secured Grade B")   
elif marks >=70 and marks <=79:
    print("User has secured Grade C") 
elif marks >=60 and marks <=69:
    print("User has secured Grade D")
elif marks <60 and marks >=0:
    print("User has failed,study again")
else:
    print("No negative values")

#Task --> Same usecase try with if-else-else usage in other way


#Voter Eligibility checkcase -->make sure to satisfy all possible conditions
#>=18 and 100 -->Access
#<18 --> no of years eligibility should tell
#negative values --> not acceptable

age = int(input("Enter the age:"))
if age>=18 and age <=100:
    print('----User has Vote Eligibility----')
    print('----Access Granted----')
elif age<18 and age >0:
    print('----User still need to get Vote Eligibility----')
    print('----User need to wait for more',(18-age),'year(s)----')
else:
    print('----Only +ve values and less than 100 Acceptable----')
    
#prefer if-elif-else....

#output --> print()-->we can pass any values also use sep and end
#Output Formatting -->old style formatting (using commas)
#% usage (%f,%d),.format() usage,fstring notation

a,b =7,9
print(a)
print(b)
print(a,b)
name = "Codegnan";batch = "DataAnalytics"
print(name,batch) #by default sep is having space
print(name,batch,sep=',')
print(name,batch,sep='----')
#end='\n', \t -->tab space
print(name,batch,end='\t')
print(a,b,end='')
print("Hyderabad")
'''
name = 'Codegnan';age=7;batch='DA-023';place='Hyderabad'
#usage of commas
print(batch,'is in',name) #variables abd msg to be separated by comm
print(name,'is in',place,'age is',age,'years')
#Old style formatting --> %d -->integer,%s-->string,%f-->float
salary = 2456.56
print("His Salary is %d"%(salary))
print("His Salary is %f"%(salary))
print("His Salary is %.1f"%(salary)) #%.1f --> rounding to 1 decimal

#.format() usage
print("{} is in {}".format(name,place)) #order matters

#fstring usage(more recommended)

print(f'{name} is in {place}')
print(f'{"srujana"} is in {name}')
 










