# Problem Statement: Given an integer N, return true if it is a palindrome else return false.

def isPalindrome(num) :
    temp = num
    rev_num = 0
    while(temp>0) :
        digit = temp%10
        rev_num = rev_num*10 + digit
        temp //= 10
    return rev_num == num 
num = int(input("Enter a number "))
if(isPalindrome(num)) :
    print(f"{num} is a palindrome")
else :
    print(f"{num} is not a palindrome")