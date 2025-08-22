# Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

# using parameterised way :
# def sum_of_n_numbers(i,n):
#     if n == 0 :
#         print(i)
#         return
#     # i += n
#     # sum_of_n_numbers(i,n-1)
#     sum_of_n_numbers(i+n,n-1)

# sum_of_n_numbers(0,5)

# using functional recursion
def sum_of_n_numbers(n) :
    if n == 0 :
        return 0
    return n + sum_of_n_numbers(n-1)
total_sum = sum_of_n_numbers(5)
print(total_sum) 