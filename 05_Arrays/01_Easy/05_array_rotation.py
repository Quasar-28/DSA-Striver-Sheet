# Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

# Left rotation by k :
# def rotate(arr,left,right) :
#     while(left<right) :
#         arr[left],arr[right] = arr[right],arr[left]
#         left += 1
#         right -= 1

# def left_rotation(arr,k) :
#     n = len(arr)
#     if k > n :
#         k = k % n
#     rotate(arr,0,k-1)
#     rotate(arr,k,n-1)
#     rotate(arr,0,n-1)


# arr = list(map(int,input("Enter elements of array : ").split()))
# k = int(input("Enter k : "))
# left_rotation(arr,k)
# print(arr)

# or (using list indexing)
# arr = list(map(int,input("Enter elements of array : ").split()))
# k = int(input("Enter k : "))
# n = len(arr)
# if k > n :
#     k %= n
# arr = arr[k:n] + arr[0:k]
# print(arr)


# right rotation by k :
# def rotate(arr,left,right) :
#     while(left<right) :
#         arr[left],arr[right] = arr[right],arr[left]
#         left += 1
#         right -= 1

# def right_rotation(arr,k) :
#     n = len(arr)
#     if k > n :
#         k %= n
#     rotate(arr,0,n-k-1)
#     rotate(arr,n-k,n-1)
#     rotate(arr,0,n-1)
# arr = list(map(int,input("Enter elements of array : ").split()))
# k = int(input("Enter k : "))
# right_rotation(arr,k)
# print(arr)

# or (using list indexing)
# arr = list(map(int,input("Enter elements of array : ").split()))
# k = int(input("Enter k : "))
# n = len(arr)
# if k > n :
#     k %= n
# arr = arr[n-k:n] + arr[0:n-k]
# print(arr)