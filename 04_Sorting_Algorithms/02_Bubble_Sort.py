"""
🔹 Idea of Bubble Sort
Bubble Sort works like bubbles rising in water 💧:
    1. Compare two neighbors.
    2. If they are in the wrong order, swap them.
    3. After one full pass, the largest element "bubbles up" to the end.
    4. Repeat this process for the remaining elements until everything is sorted.
"""

"""
🔹 Algorithm (Steps)
   1. Repeat n-1 passes over the list.
   2. In each pass:
     . Compare every adjacent pair.
     . Swap if they are in the wrong order.
   3. After each pass, the largest element is fixed at the end.
   4. Continue until sorted.
"""

# Algorithm implementation :-
arr = [13,46,24,52,20,9]
print(f"Array before sorting : {arr}")
n = len(arr)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(f"Array after sorting : {arr}")

# Optimized Bubble Sort
# Idea: Stop early if no swaps happen (array already sorted)
arr = [13,46,24,52,20,9]
print(f"Array before sorting : {arr}")
n = len(arr)
for i in range(n - 1):
    swapped = False   # flag
    
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    
    if not swapped:   # no swap → already sorted
        break
print(f"Array after sorting : {arr}")


"""
🔹 Key Points
  . Time Complexity: O(n²) (two loops).
  . Space Complexity: O(1).
  . Best case (if already sorted): O(n) with a small optimization (stop early if no swaps in a pass).
  . Good for: Learning, very simple.
  . Bad for: Large datasets (slow).
  . stable
  . in place
"""