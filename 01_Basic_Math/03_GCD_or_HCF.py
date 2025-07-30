# Problem Statement: Given two integers N1 and N2, find their greatest common divisor.

# Method 1 (brute force)
def find_GCD(num1,num2) :
    n = min(num1,num2)
    gcd = 0
    for i in range(1,n+1) :
        if (num1 % i == 0 and num2 % i == 0) :
            gcd = i
    return gcd

num1,num2 = map(lambda x : int(x) ,input("Enter two numbers ").split())
gcd = find_GCD(num1,num2)
print(f"GCD of {num1} and {num2} : {gcd}")

# Method 2 (better approach)
"""
We can optimise the time complexity of the previous approach(brute force approach). In the worst case, the loop iterates from 1 up to the minimum of N1 and N2. This could potentially result in a large number of iterations, especially when one input number is significantly larger than the other.
If we iterate from the minimum of N1 and N2 down to 1, we reduce the number of iterations because we start from the potentially largest common factor and work downwards.
The time complexity of this approach remains O(min(N1, N2)) but in practice, it will execute fewer iterations on average.
"""
def find_GCD(num1,num2) :
    n = min(num1,num2)
    gcd = 0
    for i in range(n,1) :
        if (num1 % i == 0 and num2 % i == 0) :
            gcd = i
    return gcd

num1,num2 = map(lambda x : int(x) ,input("Enter two numbers ").split())
gcd = find_GCD(num1,num2)
print(f"GCD of {num1} and {num2} : {gcd}")

# Method 3 (Optimal Approach)
def find_gcd(num1, num2):
    if num1 <= 0 or num2 <= 0:
        return None
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

num1, num2 = map(int, input("Enter two numbers: ").split())
gcd = find_gcd(num1, num2)
if gcd:
    print(f"GCD of {num1} and {num2} is: {gcd}")
else:
    print("Please enter positive integers only.")