"""
Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

Examples:
Example 1:
Input: N = 5
Output: 0 1 1 2 3 5

Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

Example 2:
Input: 6
Output: 0 1 1 2 3 5 8
Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)
"""


# Recursive function to calculate Fibonacci number
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Function to print Fibonacci series up to Nth term
def fibonacci_series_recursive(N):
    result = []
    for i in range(N + 1):  # Include Nth term
        result.append(fib(i))
    return result

# Example usage
N = int(input("Enter N: "))
print("Fibonacci series up to", N, "th term:")
print(*fibonacci_series_recursive(N))

# for calculating sum of fibonaci series upto nth index(0 based indexing)
def fib_at_ith_index(i):
    if i == 0 :
        return 0 
    if i == 1 :
        return 1 
    return fib_at_ith_index(i-1) + fib_at_ith_index(i-2)
def calculate_sum_upto_nth_index(n) :
    if n == 0 :
        return 0 
    return fib_at_ith_index(n) + calculate_sum_upto_nth_index(n-1)
print(calculate_sum_upto_nth_index(5))  # index = 5 , total terms = 6 (0,1,1,2,3,5)
