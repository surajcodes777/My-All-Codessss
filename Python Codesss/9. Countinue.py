# 1. Skip Multiplies of 3

n = int(input("Enter ending Number : "))

print("\nNumbers Expcept Multiplies of 3: ")

for i in range(1, n + 1):
    if i % 3 == 0:
        continue


    print(i,end="") 



#  2. Skip Vowels 


text = input("Enter a string : ")

print("\nWithout Vowels:")

for ch in text :
    if ch.lower() in "aeiou":
        continue

    print(ch,end="")


#  3. Skip even Numbers


n = int(input("Enter Ending Number: "))

print("\nodd Numbers: ")

for i in range(1, n + 1):
    if i % 2 == 0:
        continue

    print(i,end="")


# 4. Skip Failed Students

n = int (input("Enter a number of Students : "))   

print("\nPassed Students:")

for i in range(1, n + 1):
    marks = int(input("Enter Marks Of Students {i}:"))

    if marks < 40:
        continue

    print("Students",i,"Passed")


# 5. Skip Spaces

text = input("Enter A String : ")

print("\nWithout Spaces:")

for ch in text:
    if ch == "":
        continue

    print(ch,end="")



    