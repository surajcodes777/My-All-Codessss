
# 1. Countdown

n = int(input("Enter A Fisrt Number : "))

print("/nCountdown")

while n >= 1:
 print(n)
 n = n - 1

print("/nTime's Up!")


# 2. Guess The Number

secret = 8

while True:
 guess = int(input("/nGuess The Number : "))

 if guess == secret:
  print("Correct")
  break
 else:
  print("Wrong Guess, try again")


# 3. Password Retry

Password = "Suraj123"

while True:
 User_password = input("/nEnter Your Password : ")

 if User_password == Password:
  print("Login succesful !")
  break
 else:
  print("Wrong Password.Try Again")

# 4. Reverse Digits

num = int(input("Enter A Number : "))
reverse = 0

while num > 0:
 digit = num % 10
 reverse = reverse * 10 + digit
 num = num // 10


print("/nReverse =", reverse)