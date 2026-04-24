"""
🔹 What is Merge Sort?
. Merge sort is a divide-and-conquer sorting algorithm.
. The idea:
    1. Divide the array into two halves until each subarray has only 1 element.
    2. Conquer by recursively sorting the halves.
    3. Combine (merge) the two sorted halves into one sorted array.
"""

"""
🔹 Why does this work?
    . A single element is always "sorted".
    . If you can merge two sorted arrays efficiently, you can keep combining until the whole array is    sorted.
    . The "merge" step is where the magic happens.
"""

"""
🔹Steps of Merge Sort (Concept)
    1. Divide the array into halves:
        Keep splitting until every subarray has only 1 element.
    2. Merge the subarrays back together:
        Compare elements from both halves, and build a new sorted subarray.
    3. Continue until you have one big sorted array.
"""


# Merge sort algorithm example :

def merge(arr,low,mid,high) :
    temp_arr = []
    left = low 
    right = mid + 1
    
    # merge two sorted halves
    while left <= mid and right <= high :
        if arr[left] <= arr[right] :
            temp_arr.append(arr[left])
            left += 1
        else :
            temp_arr.append(arr[right])
            right += 1

    # remaining elements
    while(left <= mid) :
        temp_arr.append(arr[left])
        left += 1
    while(right <= high) :
        temp_arr.append(arr[right])
        right += 1
    
    # copy back to original array
    for i in range(low, high + 1) :
        arr[i] = temp_arr[i-low]

def merge_sort(arr,low,high) :
    if low == high :
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr,low,mid,high)

arr = [1,6,2,7,3,5,4]
print(f"Array before sorting : {arr}")
merge_sort(arr,0,len(arr)-1)
print(f"Array after sorting : {arr}")



"""
🔹 Time and Space Complexity
Time Complexity:
   . Divide step: O(log n) levels (array splits in half each time).
   . Merge step: O(n) work per level (every element copied once per level).
   . Total = O(n log n).
Space Complexity:
   . Needs extra space = O(n) for the temporary arrays.
   . (Unlike quicksort which can be in-place but has worst-case O(n²)).
"""

"""
Key Properties :
  . Stable Sort (because equal elements maintain order due to <=).
  . Not in-place (uses extra memory). 
  . Works well for linked lists (easy to merge without extra space). 
  . Often used in external sorting (like sorting huge files on disk).
"""