


# 1. COUNT ELEMENT
print("\n--- 1. Count Element ---")

numbers = (10, 20, 10, 30, 10, 40)

print("Tuple:", numbers)

num = int(input("Enter element to count: "))

count = numbers.count(num)

print("Element count:", count)


# 2. INDEX OF ELEMENT
print("\n--- 2. Index of Element ---")

numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)

num = int(input("Enter element: "))

if num in numbers:
    print("Index:", numbers.index(num))
else:
    print("Element not found")


# 3. TUPLE UNPACKING
print("\n--- 3. Tuple Unpacking ---")

student = ("Suraj", 19, "BCA")

name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)


# 4. CONVERT TUPLE TO LIST
print("\n--- 4. Convert Tuple to List ---")

numbers = (10, 20, 30, 40)

print("Original Tuple:", numbers)

my_list = list(numbers)

print("Converted List:", my_list)