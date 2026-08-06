'''
#sum of given numbers using for loop
price =list(map(int,input().split(',')))
total = 0
for i in price:
    total = total + i
print(total)
'''
'''
#password analyzer - upper case,lower case,digits,special characters
password = "Srujana@0324"
print(password)
a = "Srujana@0324"
upper = 0
lower = 0
digits =0
special = 0
for ch in password:
    if 'A'<= ch <='Z':
        upper +=1
    elif 'a'<= ch <='z':
        lower +=1
    elif '0'<= ch <='9':
        digits +=1
else:
    special +=1
print("upper_case",upper)
print("lower_case",lower)
print("digits",digits)
print("special_chr",special)
   
#change the domain name
email = input().split()
for mail in email:
    print(mail.split('@')[1])

'''
'''
#movies should return with index
movies = input().split(',')
i=1
for movie in movies:
    print(i,".",movie,sep="")
    i=i+1
  
#fibonacci series
n = 10
a,b = 0,1
for i in range(n):
  print(a,end=" ")
  c = a+b
  a = b
  b = c
  '''
#fibonacci with while loop
n = int(input("Enter the numbers:"))
a,b = 0,1
i = 0
while i<n:
    print(a,end=" ")
    c = a+b
    a = b
    b = c
    i+=1

  























    
    

    














