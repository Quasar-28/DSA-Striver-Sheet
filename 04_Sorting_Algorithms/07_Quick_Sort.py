# Quick sort algorithm :
# Core Idea (Divide & Conquer)
# Pick a pivot(pivot can be any element of the array)
# Place it at its correct position
# Elements:
# < pivot → left
# > pivot → right
# Recursively sort left and right parts
def partition(arr,low,high) :
    pivot = arr[low]
    i = low 
    j = high
    while(i<j) :
        while(arr[i] <= pivot and i < high) :
            i += 1
        while(arr[j] > pivot and j > low ) :
            j -= 1
        if i < j :
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j

def quick_sort(arr,low,high) :
    if low < high :
        partition_index = partition(arr,low,high)
        quick_sort(arr,low,partition_index-1)
        quick_sort(arr,partition_index+1,high)
arr = [64, 34, 25, 12, 22, 11, 90]
quick_sort(arr,0,len(arr)-1)
print(arr)