"""
Problem Statement: 
Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.
If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.
"""
# method 1 : brute force (not in place) 
# def remove_duplicates(arr) :
#     n = len(arr)
#     temp = []
#     for num in arr :
#         if num not in temp :
#             temp.append(num)
#     for i in range(0,len(temp)) :
#         arr[i] = temp[i]
#     return arr
# arr = list(map(int,input().split()))
# print(remove_duplicates(arr))


# method 2 : optimal approach (in place) : using two pointers 
# we can take advantage of the fact that array is sorted

# def remove_duplicates(nums):
#     if not nums:
#         return 0
#     i = 0  # points to last unique element
#     for j in range(1, len(nums)):
#         if nums[j] != nums[i]:
#             i += 1
#             nums[i] = nums[j]
#     return i + 1
# arr = list(map(int,input().split()))
# k = remove_duplicates(arr)
# print(arr[:k])



