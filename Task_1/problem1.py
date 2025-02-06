# Write a program that takes numbers as input from the user, terminates when the user enters -1,
# and prints the sum of all the entered numbers.
# Ex:
# Input: 4 8 15 16 23 42 -1
# Output: Sum: 108

num = int(input())
sum=0
while(num != -1):
    sum += num
    num = int(input())

print(sum)