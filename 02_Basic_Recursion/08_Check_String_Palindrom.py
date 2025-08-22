# Problem Statement: "Given a string, check if the string is palindrome or not."  A string is said to be palindrome if the reverse of the string is the same as the string.

def isPalindrome(i,st,n) :
    if i >= n//2 :
        return True
    if st[i] != st[n-i-1] : 
        return False
    return isPalindrome(i+1,st,n)
my_str = "abba"
result = isPalindrome(0,my_str,len(my_str))
print(result)