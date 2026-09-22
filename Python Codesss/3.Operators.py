
# 1. Calculator (+,-,*,/,%)

a = int(input("Enter a First number : "))
b = int(input("Enter a Second number : "))

print("Addition = ",a+b)
print("Subtract = ",a-b)
print("Multiply = ",a*b)
print("Divide = ",a/b)


# 2. Even And Odd 

num = int(input("Enter a Number : "))


if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# 3. Greatest Of 2 Numbers

a = int(input("Enter a First Number : "))
b = int(input("Enter a Second Number : "))


if a > b:
    print("Greatest Number Is = ",a)
else:
    print("Greatest Number Is = ",b)    


# 4. Vote Eligiblity

Age = int(input("Enter Your Age : "))



if Age > 18:
    print("Yes You Are Eligible To Vote")
else:
    print("No You Are Not Eligible To Vote")        