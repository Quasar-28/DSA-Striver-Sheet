# Problem: Print your Name N times using recursion

def print_name(i,n) :
    if i > n :
        return
    print("Roger")
    print_name(i+1,n)
print_name(1,5)

# or 

# def print_name(n) :
#     if n == 0 :
#         return
#     print("Roger")
#     print_name(n-1)
# print_name(5)
