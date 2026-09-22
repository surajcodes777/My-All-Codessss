
# 1. PHONE BOOK
print("\n--- 1. Phone Book ---")

phone_book = {
    "Rahul": "9876543210",
    "Aman": "9876501234",
    "Rohit": "9876512345"
}

name = input("Enter name: ")

if name in phone_book:
    print("Phone Number:", phone_book[name])
else:
    print("Contact not found")


# 2. STUDENT INFORMATION
print("\n--- 2. Student Information ---")

student = {
    "name": input("Enter student name: "),
    "age": int(input("Enter age: ")),
    "course": input("Enter course: "),
    "marks": int(input("Enter marks: "))
}

print("\nStudent Information:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])


# 3. UPDATE MARKS
print("\n--- 3. Update Marks ---")

student["marks"] = int(input("Enter new marks: "))

print("Updated Marks:", student["marks"])


# 4. SEARCH KEY
print("\n--- 4. Search Key ---")

key = input("Enter key to search: ")

if key in student:
    print("Key found!")
    print("Value:", student[key])
else:
    print("Key not found")




