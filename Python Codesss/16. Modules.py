# 1. RANDOM NUMBER
print("\n--- 9. Random Number ---")

import random

num = random.randint(1, 100)

print("Random Number:", num)



# 2. OTP GENERATOR
print("\n--- 10. OTP Generator ---")

import random

otp = random.randint(100000, 999999)

print("Your OTP is:", otp)


# 3. DATE AND TIME
print("\n--- 11. Date and Time ---")

import datetime

now = datetime.datetime.now()

print("Current Date and Time:", now)


# 4. MATH CALCULATOR
print("\n--- 12. Math Calculator ---")

import math

num = float(input("Enter a number: "))

print("Square Root:", math.sqrt(num))
print("Power 2:", math.pow(num, 2))
print("Ceiling:", math.ceil(num))
print("Floor:", math.floor(num))
