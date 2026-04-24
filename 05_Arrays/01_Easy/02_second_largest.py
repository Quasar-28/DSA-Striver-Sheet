# Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.


# method 1 : using two consecutive loops
# def find_largest_second_largest_elements(arr) :
#     n = len(arr)
#     if n == 0 :
#         return -1 
#     largest = arr[0]
#     second_largest = arr[1]
#     for i in range(0,len(arr)) :
#         if arr[i] > largest :
#             largest = arr[i]
#     for i in range(0,len(arr)) :
#         if (arr[i] > second_largest and arr[i] != largest) :
#             second_largest = arr[i]
#     return largest,second_largest


# method 2 : using single loop
# def find_largest_second_largest_elements(arr) :
#     n = len(arr)
#     if n == 0 :
#         return -1 
#     if n == 1 :
#         return arr[0],arr[0]
#     largest = arr[0]
#     second_largest = arr[1]
#     for i in range(0,len(arr)) : 
#         if arr[i] > largest :
#             second_largest = largest
#             largest = arr[i]
#         elif arr[i] > second_largest :
#             second_largest = arr[i]
#     return largest,second_largest


# method 3 : using sorting : by using built in sort()
# def find_largest_second_largest_elements(arr) :
#     arr.sort()
#     return arr[-1],arr[-2]


arr = list(map(int,input().split()))
print(find_largest_second_largest_elements(arr))