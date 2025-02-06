# Problem 6
#Write a Python program that takes a positive integer as input and checks whether it is a perfect number or not. 
# A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.
# Ex:
# Input: 28
# Output: 28 is a perfect number.

num = int(input())
divisor_sum = 0
for i in range(1, num):
    if num % i == 0:
        divisor_sum += i

if num == divisor_sum:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")