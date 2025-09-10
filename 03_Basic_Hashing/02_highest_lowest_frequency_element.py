# Problem Statement: Given an array of size N. Find the highest and lowest frequency element.
"""
Example 1:
Input: array[] = {10,5,10,15,10,5}
Output: 10 15
Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.
"""
# Solution : 
# Method 1 : first finding frequencies of elements using hash map and then finding the lowest and highest frequency
array = [10,5,10,15,10,5]
hash_map = {}
for num in array :
    if num not in hash_map :
        hash_map[num] = 1
    else :
        hash_map[num] += 1
# min_freq = min(hash_map.values())
# max_freq = max(hash_map.values())
# for num , count in hash_map.items() :
#     if count == min_freq : 
#         print(f"Element with minimum frquency is {num} with count {count}")
#     elif count == max_freq : 
#         print(f"Element with maximum frquency is {num} with count {count}")
