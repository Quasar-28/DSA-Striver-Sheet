# Problem Statement: Given an array, we have to find the largest element in the array.
# arr = []
# n = int(input("Enter length of array : "))
arr = list(map(int, input().split()))
largest_element = arr[0]
for i in range(0,len(arr)) :
    if arr[i] > largest_element :
        largest_element = arr[i]
print(largest_element)

# or we can use built in function max(arr) to get largest_element
largest_element = max(arr)
print(largest_element)