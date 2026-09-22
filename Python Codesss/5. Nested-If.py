
# 1. Student Grade

Marks = int(input("Enter Your Marks : "))

if Marks >= 0:
    if Marks >= 90:
        print("Grade A")
    elif Marks >= 80:
        print("Grade B")
    elif Marks >= 70:
        print("Grade C")
    elif Marks >= 60:
        print("Grade D")
    elif Marks >= 50:
        print("Grade E")
    else:
        print("Fail")
else:
    print("Invalid Marks")


# 2. Employee Bonus

Salary = int(input("Enter Your Salary : "))
Years = int(input("Enter Year Of Your Service : "))

if Years >= 5:
    if Salary >= 500000:
        bonus = Salary * 0.10
    else:
        bonus = Salary * 0.05

    print("Bonus:",bonus)
else:
    print("Not Eligible For Bonus")

# 3. Project Experience Level

projects = int(input("Enter Number Of Projects : "))

if projects >= 0:
    if projects >= 10:
        print("Expert")
    if projects >= 6:
        print("Intermediate")
    if projects >= 1:
        print("Beginner")
    else:
        print("No Experiences")
else:
    print("Invalid Input")

# 4. Loan Eligiblity

age = int(input("Enter Your Age : "))    
Salary = int(input("Enter Your Monthly Salary : "))

if age >= 18:
    if Salary >= 30000:
        print("Loan Eligible")
    else:
        print("Not Eligible: Sorry Your Salary Is Tooo Loww ! ")
else:
    print("Not Eligible: Sorry Your Age Is Too Loww !")