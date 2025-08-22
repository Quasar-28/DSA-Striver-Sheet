# Recursion is a phenomenon when a function calls itself indefinitely until a specified condition(known as base condition) is fulfilled.
def recursive_function() :
    print("Calling itself....")
    recursive_function()
recursive_function()
# Since in the above function there is no stopping condition so we will get RecursionError: maximum recursion depth exceeded
# here is example of recursion with the base condition
count = 0
def count_up_to_3() :
    global count
    if count == 3 :
        return
    print(count)
    count+=1
    count_up_to_3()
count_up_to_3()
# here the base condition is when count reaches to 3