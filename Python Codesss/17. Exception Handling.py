# 1. DIVIDE BY ZERO
print("\n--- 13. Divide by Zero ---")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")


# 2. FILE NOT FOUND
print("\n--- 14. File Not Found ---")

try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found!")


# 3. MULTIPLE EXCEPTIONS
print("\n--- 15. Multiple Exceptions ---")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ValueError:
    print("Please enter numbers only!")

except ZeroDivisionError:
    print("Cannot divide by zero!")


# 4. FINALLY BLOCK
print("\n--- 16. Finally Block ---")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero!")

finally:
    print("This block always executes.")