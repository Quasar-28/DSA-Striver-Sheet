def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)

    # Base case
    if n == 1:
        return arr

    # One pass (largest element goes to end)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]  # swap

    # Recursively call on remaining array
    return bubble_sort_recursive(arr, n - 1)


# Example
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted (recursive) using bubble sort:", bubble_sort_recursive(arr))


# more optimised recursive code for bubble sort : 
def bubble_sort_recursive_optimised(arr2, n=None):
    if n is None:
        n = len(arr2)

    # Base case
    if n == 1:
        return arr2

    swapped = False

    # One pass of bubble sort
    for i in range(n - 1):
        if arr2[i] > arr2[i + 1]:
            arr2[i], arr2[i + 1] = arr2[i + 1], arr2[i]  # swap
            swapped = True

    # If no elements were swapped, array is sorted
    if not swapped:
        return arr2

    # Recur for remaining array
    return bubble_sort_recursive_optimised(arr2, n - 1)


# Example
arr2 = [5, 1, 4, 2, 8]
print("Sorted array:", bubble_sort_recursive_optimised(arr2))

