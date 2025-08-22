# Problem: Print from 1 to N using Recursion
def print_upto_n(i,n) :
    if i>n :
        return
    print(i)
    print_upto_n(i+1,n)
print_upto_n(1,5)


# using backtracking
def print_upto_n(i,n) :
    if i>n :
        return
    print_upto_n(i+1,n)
    print(n-i+1)
print_upto_n(1,5)