#guess the secret code using while loop
'''

secret_code = "0330"
guess = input("Enter the code:")
while guess != secret_code:
    print("wrong code")
    guess = input("Enter the code:")
print("correct code")

#OTP verification
otp = "2024"
max_attempts = 7
current_attempt = 0
while current_attempt < max_attempts:
    entered_otp = input("Enter the otp:")
    if entered_otp == otp:
      print("otp is correct")
      break
    else:
        print("entered otp is wrong")
        current_attempt +=1
else:
    print("otp is wrong,try again")

#count of orders
order = input("Enter the order:")
count = 0
while order!= "exit":
    count +=1
    order = input("Enter the order:")
print("total number of orders",count)
'''
#
secret = "python"
current = 0
max_attempts = 3
while current < max_attempts:
    a = input()
    if (a==secret):
        print("access again")
        break
    else:
        remaining = max_attempts - current
        print(f'wrong guess')
        current += 1 
else:
    print("chances over")
  




















