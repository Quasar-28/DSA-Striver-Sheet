# Problem: Print from N to 1 using Recursion
# def print_upto_n_in_reverse(n) :
#     if n==0 :
#         return
#     print(n)
#     print_upto_n_in_reverse(n-1)
# print_upto_n_in_reverse(5)

# using backtracking
def print_upto_n_in_reverse(n,i) :
    if i>n :
        return
    print_upto_n_in_reverse(n,i+1)
    print(i)
print_upto_n_in_reverse(5,1)
