# Problem Statement: Given an integer N, return all divisors of N.
# method 1(brute force approch) :
num = int(input("Enter a number : "))
for i in range(1,num+1) : 
    if num % i == 0 : 
        print(i,end=" ")

# method 2(Optimal Approach) : 
import math as m
divisors_list = []
num = int(input("Enter a number : "))
for i in range(1,int(m.sqrt(num)+1)) : 
    if num % i == 0 : 
        if i == num//i : 
            divisors_list.append(i)
            continue
        divisors_list.extend([i,num//i])
print(sorted(divisors_list))
# without math module we can write the condition as for i in range(1,int(num**0.5)+1)