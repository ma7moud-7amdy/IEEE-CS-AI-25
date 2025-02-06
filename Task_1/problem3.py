# Problem 3
# Write a Python program that takes a positive integer as input and prints the sum of its digits.
# Ex:
# Input: 123
# Output: The sum of digits is 6 (1 + 2 + 3)

num = input().strip()
sum=0
for  s in num :
    sum += int(s)
print(f"The sum of digits is {sum}")
