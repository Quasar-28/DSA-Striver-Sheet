"""
🔹 Idea of Insertion Sort
Think about arranging playing cards in your hand 🃏:
  . You pick one card at a time from the deck.
  . Insert it into the correct position among the already sorted cards in your hand.
  . Keep doing this until all cards are arranged.
"""

"""
🔹 Algorithm (Steps)
  1. Assume the first element is sorted.
  2. Pick the next element.
  3. Compare it with elements in the sorted part (move backward).
  4. Shift elements if needed to make space.
  5. Insert the element at the correct position.
  6. Repeat until all elements are sorted.
"""

# For example : 
arr = [13,46,24,52,20,9]
print(f"Array before sorting : {arr}")
n = len(arr)
for i in range(1, n):
    key = arr[i]  # Element to insert
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]   # Shift elements to right
        j -= 1
    arr[j + 1] = key
print(f"Array after sorting : {arr}")


# Time Complexity
# Best: O(n) (already sorted)
# Average: O(n²)
# Worst: O(n²)

# Space Complexity
# O(1) (in-place)

# Key Points :
# Stable sort ✅
# In-place ✅
# Good for small datasets ✅
# Used in real systems (hybrid sorts like Timsort)
# When to use
# Small arrays
# Nearly sorted data