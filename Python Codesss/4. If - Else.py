
# 1. Pass / Fail 

Marks = int(input("Enter Your Marks : "))


if Marks > 30:
    print("Pass")
else:
    print("Fail")


# 2. Postive / Negative 

Num = int(input("Enter A Number : "))


if  Num > 0:
    print("Postive")
elif Num < 0:
    print("Negative") 
else:
    print("Zero")   



# 3. Greatest Of 3 Numbers

a = int(input("Enter a First Number : "))
b = int(input("Enter a Second Number : "))
c = int(input("Enter a Third Number : "))


if a > b and a > c:
    print("Greatest Number Is = ",a)
elif b < a and b > c:
    print("Greatest Number Is = ",b)
else:
    print("Greatest Number Is = ",c)    


# 4. Discount Eligibilty

amount = int(input("Enter amount : "))



if amount > 5000:
    print("Your Discount Is Eligible")

else:
    print("Your Discount Is Not Eligible")         