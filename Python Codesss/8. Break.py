
# 1. Stop At 50

for i in range(1,101):
    if i == 50:
        break
    print(i)

# 2.  Exit On Password

while True:
    password = input("/nEnter Password : ")

    if password == "Exit":
        print("Program Stopped")
        break

    print("You Entered:",password)   


# 3. Stop When Number Found

for i in range(1,101):
    if i == 50:
        print("/nNumber Found:",i)
        break

    print(i)

# 4. Menu Exit
 
while True:
 print("/n-- MENU ---")   
 print("1. Hello")
 print("2. Python")    
 print("3. Exit")  

 choice = int(input("/nEnter Your Choice : "))

 if choice == 1:
     print("Hello")
 
 if choice == 2:
     print("I Am Learning Python Codes")

 if choice == 3:
     print("Programs Exited")
     break
 else:
     print("Invalid Choice!")
            