# Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

# method 1 : Brute force : O(n^2) time complexity
# def is_sorted(arr, n):
#     for i in range(n):
#         for j in range(i + 1, n):
#             # If any element is smaller than the previous one, return false
#             if arr[j] < arr[i]:
#                 return False
#     return True  # Return true if no unsorted elements are found


# method 2 : Optimal approach : O(n) time complexity
# def is_sorted(arr) :
#     n = len(arr)
#     sorted = True
#     for i in range(0,n-1) :
#         if arr[i] > arr[i+1] :
#             sorted = False
#             break
#     return sorted

# arr = list(map(int,input().split()))
# print(is_sorted(arr))