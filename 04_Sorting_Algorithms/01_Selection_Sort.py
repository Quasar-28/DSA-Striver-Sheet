"""
🔹 Idea of Selection Sort :-
Selection Sort works like how we arrange books by size or cards in order:
    - Look at the whole list and find the smallest item.
    - Put it in the first position.
    - Then look at the rest of the list, find the next smallest, and put it in the second position.
    - Keep repeating until everything is in order.
"""
"""
🔹 Algorithm (Steps)
  1. Start from the first element.
  2. Find the smallest element in the remaining array.
  3. Swap it with the current element.
  4. Move to the next position and repeat until the array is sorted.
"""

# For example : 

arr = [9,13,46,24,52,20]
print(f"Array before sorting : {arr}")
# Selection sort algorithm implementation :-
for i in range(len(arr)-1) :
    min_element_index = i
    for j in range(i+1,len(arr)) :
        if arr[j] < arr[min_element_index]  :
            min_element_index = j
    arr[i] , arr[min_element_index] = arr[min_element_index] , arr[i]
print(f"Array after sorting : {arr}")



"""
🔹 Key Points
  1. Time Complexity: O(n²) (because of two loops).
  2. Space Complexity: O(1) (no extra space needed).
  3. Good for: Small arrays, easy to understand.
  4. Bad for: Large arrays (slow compared to better algorithms like quicksort, mergesort).
  5. In-place (does not use extra memory ,Sorting happens inside same array, no new array created)
  6. Not stable(it does not keep the relative order of equal elements same.)
"""