# 1. Add Item In Lists

Items = ["Apple", "Banana","Mango"]

print("Old List:", Items)

New_Item = input("\nEnter Item To Add : ")

Items.append(New_Item)

print("\nUpdated List:", Items)

# 2. Remove Item In Lists

Items = ["Apple","Banana","Mango","Orange"]

print("Old List:", Items)

Remove_Items = input("\nEnter Item To Remove: ")

if Remove_Items in Items:
    Items.remove(Remove_Items)
    print("\nUpdated List:",Items)
else:
    ("\nItem Not Found")

# 3. Largest Element In List

Numbers = []

m = int(input("Enter Number Of Elements: "))

for i in range(Numbers):
    Numbers.append(Numbers)

print("\nList:",Numbers)

largest = max(Numbers)

print("Largest element:",largest)

# 4. Sum Of List

Numbers = []

n = int(input("Enter Numbers Of Elements : "))

for i in range(Numbers):
    Numbers= int(input("Enter Numbers: "))
    Numbers.append(Numbers)

    print("\nList:",Numbers)

    Total = sum(Numbers)

    print("Sum Of List:", Total)