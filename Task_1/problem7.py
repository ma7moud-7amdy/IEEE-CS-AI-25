# Problem 7
#Write a Python program that takes a positive integer as input and finds its prime factors.
# Input: 36
# Output: Prime Factors: 2, 3

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int (input())
for x in range(2 , num+1):
    if(num % x == 0 and is_prime(x)):
        print(x,end=", ")
print("\b\b ")