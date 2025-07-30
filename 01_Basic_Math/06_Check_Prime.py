"""
Problem Statement: Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.
"""
# method 1 (brute force approach) :
# using for loop
def is_prime(num) :
    if num < 2 : 
        return False
    for i in range(2,num) : 
        if num % i == 0 : 
            return False
    return True

# using no of factors : 
# def is_prime(num) :
#     if num < 2 : 
#         return False
#     count = 2 
#     for i in range(2,num) : 
#         if num % i == 0 :
#             count += 1
#         if count > 2 : 
#             break
#     if count>2 :
#         return False
#     return True

# we can use any one of the above two functions  
num = int(input("Enter a number : "))
if is_prime(num) :
    print(f"{num} is a prime number")
else : 
    print(f"{num} is not a prime number")


# Method 2 (Optimal approch) :
import math as m
def is_prime(num) :
    if num < 2 : 
        return False
    for i in range(2,int(m.sqrt(num))+1) : 
        if num % i == 0 : 
            return False
    return True
num = int(input("Enter a number : "))
if is_prime(num) :
    print(f"{num} is a prime number")
else : 
    print(f"{num} is not a prime number")
