'''
#swapping
a = 5
b = 6
print(a,b)
a,b = b,a
print(a,b)

#positive r negative
num = int(input("Enter the number:"))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

#ATM    
num = int(input("Enter the number:"))
if num >=1000:
    prin1t("withdraw")
elif num <0:
    print("no balance")
else:
    print("should maintain minimum 1000 balance")

#Grade Checker
marks = int(input("Enter the student marks:"))
if marks >=100:
    print("Invalid marks entered,entered marks should be greater than 0 and less than 100")
elif marks >=90 and marks <=100:
    print("Student Grade = A")
    print("Remark:'A' --> Outstanding!")
elif marks >=80 and marks <=89:
    print("Student Grade = B")
    print("Remark:'B' --> Excellent!")
elif marks >=70 and marks <=79:
    print("Student Grade = C")
    print("Remark:'C' --> Good!")
elif marks >=60 and marks <=69:
    print("Student Grade = D")
    print("Remark:'D' --> Fair,needs improvement!")
elif marks >=50 and marks <=59:
    print("Student Grade = E")
    print("Remark:'E' --> Poor,need serios improvement!" )
elif marks <50:
    print("Failed,needs to reappear")
else:
    print("Invalid marks entered")

#Even odd checker
number = int(input("Enter the Number:"))
if number == 0:
    print("Zero is neither even nor odd")
elif number <0 and number %2==0:
    print("Negative even Number")
elif number <0 and number %2 !=0:
    print("Negative odd Number")
elif number >0 and number %2==0:
    print("Even Number")
elif number %2 !=0:
    print("Odd Number")
else:
    print("Invalid Input")

#Season Identifieer
month = int(input("Enter the Month Number"))
if month <1:
    print("Month Number should be in between 1 to 12")
elif month==12 or month==1 or month==2:
    print("Season = Winter")
elif month==3 or month==4 or month==5:
    print("Season - Spring")
elif month==6 or month==7 or month==8:
    print("Season = Summer")
elif month==9 or month==10 or month==11:
    print("Season = Autumn")
else:
    print("Invalid Month Entered")
'''    
result = 0
for i in range(6):
    result = result+i
print(f'sum of 5 numbers is {result}')    



























    
                    
    
    











