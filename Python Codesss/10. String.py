# 1. Skip Multiples of 3

n = int(input("Enter Ending Number : "))

print("\nNumbers Expect Multiples of 3: ")

for i in range(1, n + 1):
    if i % 3 == 0:
     continue

    print(i, end=" ")

# 2. Skip Vowels

text = input("Enter A String: ")

print("\nWithout Vowels: ")

for ch in text:
   if ch.lower() in "aeiou":
      continue

   print(ch, end=" ")


# 3. Skip Even Numbers


n = int(input("Enter Number: "))

print("\nOdd Numbers: ")

for i in range(1,n+1):
   if i % 2 == 0:
      continue

   print(i, end=" ")


# 4. Skip Failed Students


n = int(input("Enter Number Of Students: "))

print("\nPassed Students: ")

for i in range(1, n + 1):
   Marks = int(input("Enter Marks Of Students{i}:"))

   if Marks > 40:
      continue

   print("Students", i, "Passed")