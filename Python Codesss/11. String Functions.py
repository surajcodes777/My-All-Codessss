# 1. Reverse String
text = input("Enter String: ")

reverse = text[::-1]

print("\nReverse String",reverse)

# 2. Palindrome

text = input("Enter String: ")

Reverse = text[::-1]

if text == Reverse:
    print("\nPalindrome")
else:
    print("\nNot Palindrome")

# 3. Count Vowels


Text = input("Enter A String: ")

Count = 0

for ch in text:
    if ch.lower() in "aeiou":
        Count = Count + 1

print("\nTotal Vowels:",Count)

# 4. Count Words

Text = input("Enter A Sentence: ")

Words = Text.split()

print("nTotal Words:", len(Words))