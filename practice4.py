#Armstrong Number #returns the same given number

#using for loop:
n = int(input("Enter the number:"))
sum = 0
temp = n
digits = len(str(n))
for i in range(digits):
    digit = temp%10
    sum=sum+digit**3
    temp //=10
if sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

#using while loop:
n = int(input("Enter the number:"))
sum = 0
temp =n
digits = len(str(n))
while temp>0:
    digit = temp%10
    sum=sum+digit**3
    temp //=10
if sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")










