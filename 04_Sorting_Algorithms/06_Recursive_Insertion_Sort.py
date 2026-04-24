# Insertion sort algo using recursion
def recursive_insertion_sort(arr, n):
    # Base case: single element is always sorted
    if n <= 1:
        return

    # Sort first n-1 elements
    recursive_insertion_sort(arr, n-1)

    # Insert last element at its correct position
    last = arr[n-1]
    j = n-2

    # Shift elements of arr[0..n-2], that are greater than last
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = last
arr = [64, 34, 25, 12, 22, 11, 90]
recursive_insertion_sort(arr,len(arr))
print(arr)