# Problem Statement: Given an integer N, return the number of digits in N.

# Method 1 (brute force approach)
def count_digits(num) :
    temp = num
    count = 0
    while(temp>0) :
        # temp%10
        count+=1
        temp //=10
    return count
N = int(input("enter number "))
count = count_digits(N)
print(f"No of digits in {N} : {count}")


# Method 2 (Optimal approach)
import math as m
N = int(input("enter number "))
print(int(m.log10(N)+1))

# Method 3 (edge cases included) :
def count_digits(num) :
    if num == 0 :
        return 1
    elif num < 0 :
        temp = -num
    else :
        temp = num
    count = 0
    while(temp>0) :
        count+=1
        temp //=10
    return count
N = int(input("enter number "))
count = count_digits(N)
print(f"No of digits in {N} : {count}")