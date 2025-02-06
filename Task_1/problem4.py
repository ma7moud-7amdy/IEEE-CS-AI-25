# Write a Python program that takes a sentence as input and prints the sentence with each word reversed.
# Ex:
# Input: "Hello World"
# Output: "olleH dlroW"


original = input().split()
newStr=""
for subStr in original:
    newStr+= subStr[::-1] + " "

print(newStr[0:len(newStr)-1])