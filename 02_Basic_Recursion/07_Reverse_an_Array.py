# Problem Statement : You are given an array. The task is to reverse the array and print it. 

# using a vacant array :
# def reverse_array(arr, n):
#     ans = [0] * n
#     for i in range(n - 1, -1, -1):
#         ans[n - i - 1] = arr[i]
#     return ans

# arr = [1,2,3,4,5]
# ans = reverse_array(arr,len(arr))
# print(ans)

# using two pointers : 
# def reverse_array(l,r,arr) :
#     if l>=r : 
#         return
#     arr[l],arr[r] = arr[r],arr[l]
#     reverse_array(l+1,r-1,arr)
# arr = [1,2,3,4,5]
# reverse_array(0,len(arr)-1,arr)
# print(arr)

# using just a single pointer :
def reverse_array(i,arr,n) :
    if i>=n//2 : 
        return
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    reverse_array(i+1,arr,n)
arr = [1,2,3,4,5]
reverse_array(0,arr,len(arr))
print(arr)
