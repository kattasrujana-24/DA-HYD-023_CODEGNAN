'''
Control Statements --> which contorl the flow of execution of the program
                      -->Conditional Statements --> if,elif,else...
                      -->Repetition Statements(Loops) --> for,while,(for with else)(while with else)
                      -->Jumping Statements --> break,continue,pass4
'''
#Loops --> Loops are helpful for repetition (Automative tasks)
#for keyword will be helpfyl to iterate over a sequence/range
#syntax for (for keyword):
'''
for <temp_var in sequence/range:
    statement(s)....
    ........

#range(stop)-->default o and ends at stop -1
#range(start,stop,step)
#by default range pciks 0 as starting value
for i in range(10):
   print(i)'''
'''
#In above case we got 10 iterations
for i in range(1,10):
    #if i > 5:
        #print(f'Value of i is -->{i}')
    #Now i want to get only even numbers with above condition
    if i > 5 and i%2 == 0:
        print(f'Final Value of i is --> {i}')
'''
'''
#range(start,stop,step) -->here stop-->interval...
for i in range(1,10,2):
    print(i)
    print("Done")

for i in range(10,1,-1):
    print(i)

#print -10 to -1
for i in range(-10,0,1):
    print(i)
    
#[] --> we generally lists
names = ['srujana','rashmitha','akshaya']
print(len(names)) #len(obj) --> returns the number of items in a container
for name in names:
    print(names)
    print(f'student name is {names}')
    if name == "srujana":
        print(f"student name is {name}")

#Calculate the sum of first 10 numbers
#first understand your input --> range(11) -->10 numbers
#second understand your output -->sum(number)
#third we need to map the logic

result = 0 #target value
for i in range (11):
    #print(i)
    #print(f'result is {i+i}')
    result = result + i #result +=i
    #print(f'Now the result is {result}')
    print(f'sum of 10 numbers is {result}')

#sum of first 10 even numbers    
result = 0 #target value
for i in range (21):
    if i %2 == 0:
        print(i)
        result = result + i #result +=i
print(f'sum of 10 even numbers is {result}')
'''
#Understand the loops with Fitness Streak example
#work_out --> 1,work_out_missed --> 0

work_log = [0,1,1,1,0,1,0]
#result variable -->longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
      #print(day)
      current_streak = current_streak + 1
      if current_streak > longest_streak:
          longest_streak = current_streak
    else:
        current_streak = 0 #streak breaks
print(f'longest_streak is {longest_streak}')

           
    















        
   
                                                                                    
