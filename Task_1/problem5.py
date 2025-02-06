# Problem 5
# Write a Python program that takes a positive integer as input and prints all odd numbers from 1 to that integer.
# Ex:
# Input: 10
# Output: 1 3 5 7 9

num = int( input() )
for i in range(1 , num+1 , 2):
    print(i , end=" ")