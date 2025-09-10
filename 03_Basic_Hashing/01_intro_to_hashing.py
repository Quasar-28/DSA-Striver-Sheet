# number hashing :
# here we take size of the hash array equal to max. element in given array and intialise the hash array with zero.
# for e.g;
my_array = [1,3,2,3,1,4]
hash_array = [0] * (max(my_array)+1) # [0,0,0,0]
for i in my_array :
    hash_array[i] += 1
# print(hash_array)
for num in range(len(hash_array)) :
    if hash_array[num] == 0 : continue
    print(f"{num} appears {hash_array[num]} times in the array ")

# character hashing :-
# assuming all alphabets are in lower case 
# tracking count of characters present in the array 
# we will create a hash array using ascii value 
character_array = ['a','h','b','a','b','d','d','f']
chr_hash_array = [0] * 26
for char in character_array :
    chr_hash_array[ord(char) - 97] += 1
# print(chr_hash_array)
for i in range(len(chr_hash_array)) :
    if chr_hash_array[i] == 0 : continue
    char = chr(i+97)
    print(f"{char} appears {chr_hash_array[i]} times in the character array")

# similarly we can do the same for uppercase alphabets
# for all characters we can make array of size 256 and map them as per their ascii number

#  hashing using hash map (in python it is dictionary)
# hashing numbers using hash map
arr = [1,4,7,5,4,7,1,1]
hash_map = {}
for num in arr :
    if num not in hash_map :
        hash_map[num] = 1 
    else :
        hash_map[num] += 1
# print(hash_map)
for num,count in hash_map.items() :
    print(f"{num} : {count}")
    
# hashing characters using hash map
character_array = ['a','h','b','a','b','d','d','f']
char_hash_map = {}
for char in character_array :
    if char not in char_hash_map :
        char_hash_map[char] = 1
    else :
        char_hash_map[char] += 1
# print(char_hash_map)
for char , count in char_hash_map.items() :
    print(f"{char} : {count}")