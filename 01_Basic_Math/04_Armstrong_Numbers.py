# Problem Statement: Given an integer N, return true it is an Armstrong number otherwise return false.
#   Example 1:
#     Input:N = 153       
#     Output: True          
#     Explanation: 1^3+5^3+3^3 = 1 + 125 + 27 = 153

import math as m
def isArmstrong(num) :
    n = int(m.log10(num) + 1)
    total_sum = 0
    temp = num 
    while(temp>0) :
        digit = temp % 10 
        total_sum = total_sum + digit**n
        temp //= 10
    return total_sum == num
num = int(input("Enter a number : "))
if(isArmstrong(num)) :
    print(f"{num} is armstrong number")
else :
    print(f"{num} is not armstrong number")