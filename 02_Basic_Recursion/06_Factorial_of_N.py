# Problem Statement: Given a number X,  print its factorial.
def factorial_of_N(n) :
    if n == 1 :
        return 1 
    return n * factorial_of_N(n-1)
factorial_result = factorial_of_N(5)
print(factorial_result)