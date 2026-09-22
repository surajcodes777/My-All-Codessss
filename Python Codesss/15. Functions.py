 # 1. CALCULATOR FUNCTION
print("\n--- 5. Calculator Function ---")

def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Invalid operator"


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

print("Result:", calculator(a, b, operator))


# 2. SQUARE FUNCTION
print("\n--- 6. Square Function ---")

def square(n):
    return n * n


num = int(input("Enter a number: "))

print("Square:", square(num))


# 3. FACTORIAL FUNCTION
print("\n--- 7. Factorial Function ---")

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


num = int(input("Enter a number: "))

print("Factorial:", factorial(num))


# 4. PRIME FUNCTION
print("\n--- 8. Prime Function ---")

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")