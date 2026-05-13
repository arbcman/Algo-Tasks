""" 
----------------------------|
Psuedocode For Non-Recursive|
----------------------------|

  FUNCTION wisort(arr):
 //Input: Array of integers
 //Output: Array arranged in [low, high, low, high, ...] pattern
     FOR i <- 1 TO length(arr) - 1 DO
         IF (i is even AND arr[i] > arr[i - 1]) OR
            (i is odd  AND arr[i] < arr[i - 1]) THEN
               SWAP arr[i] WITH arr[i - 1]
     RETURN arr

---------------|
Time complexity|----> T(n)=(n−1)⋅O(1)= O(n)
---------------|
"""

print("Non-Recursive Implementation:")

def wisort(arr):
    for i in range(1,len(arr)):
        # if statment is the main opperation will happen (len(arr))times [n]
        if ((i%2==0 and arr[i] > arr[i-1]) or #if even and arr[current] > arr[prev]:
        (i%2==1 and arr[i] < arr[i-1])): #if odd and arr[current] < arr[prev]:
            arr[i],arr[i-1]=arr[i-1],arr[i] # performing swap
    return arr
#///////////////TEST
print("using wisort: ",wisort([1,3,2,2,3,1]))
print("using wisort: ",wisort([1,5,1,1,6,4]))
print("---------------------------------------")
""" 
------------------------|
Psuedocode For Recursive|
------------------------|

  FUNCTION reqwisort(arr,i=1(predefined)):
    //Input: Array of integers
    //Output: Array arranged in [low, high, low, high, ...] pattern
     IF i>=len(arr):
        RETURN arr
     IF (i is even AND arr[i] > arr[i - 1]) OR
           (i is odd  AND arr[i] < arr[i - 1]) THEN
           SWAP arr[i] WITH arr[i - 1]
     RETURN reqwisort(arr, i + 1)

---------------|
Time complexity|----> T(n)=T(n−1)+O(1) =  O(n)
---------------|
"""

print("Recursive Implementation:")

def reqwisort(arr,i=1):
    if i>=len(arr):# base case: this is the exit condition that happens (len(arr)) times [n]
        return arr
    # if statment is the main operation to check the [low, high] pattern and will happen (len(arr)) times [n]
    if ((i%2==0 and arr[i] > arr[i-1]) or#condition to check if the current element is in the correct order
        (i%2==1 and arr[i] < arr[i-1])):# based on its index (even or odd)
            arr[i],arr[i-1]=arr[i-1],arr[i]
    return reqwisort(arr,i+1)# recursive call: moves to the next index, creating T(n-1) logic
#///////////////TEST
print("using reqwisort: ",reqwisort([1,3,2,2,3,1]))
print("using reqwisort: ",reqwisort([1,5,1,1,6,4]))
print("---------------------------------------")


""" 
--------------------------------
Comparison of Time Complexities:
--------------------------------
Both the non-recursive and recursive implementations have the same time complexity of O(n),

The Non-recursive algorithm has a single loop that runs from i = 1 to n - 1
which means it executes (n − 1) iterations, inside each iteration a Constant number of Operations
One If condition (the main) Possibly a swap which also constant 
each iteration is O(1) ----> T(n)=(n−1)⋅O(1)= O(n).
Similary in the recursive implementation, each recursive call:
Checks the base case -> constant time
Evaluates the condition -> constant time
Possibly performs one swap -> constant time
Calls itself with i + 1
So each call does O(1) -----> T(n)=T(n−1)+O(1) =  O(n)  
--------------------------------"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # append the rest (if one side length > the other)
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

def newwisort(nums):
    # using merge sort 
    ms_nums=merge_sort(nums)
    n = len(ms_nums)
    mid = n // 2

    left = nums[:mid][::-1]
    right = nums[mid:][::-1]
    
    result = []
    i=j=0
    
    for k in range(n):
        if k % 2 == 0:  # even index so (take from left)
            if i < len(left):
                result.append(left[i])
                i += 1
            elif j < len(right):  # left is exhausted so (take from right)
                result.append(right[j])
                j += 1
        else:  # odd index so (take from right)
            if j < len(right):
                result.append(right[j])
                j += 1
            elif i < len(left):  # right is exhausted so (take from left)
                result.append(left[i])
                i += 1
                
    return result
# Total time complexity
# Merge sort => O(n log n)
# Slicing & reversing => O(n)
# Interleaving => O(n)
# O(nlogn) + O(n) + O(n) = O(nlogn)

# Dominant term: O(n log n)

print("merge_sort then wiggle Implementation:")
nums = [1,2,3,4,5,6]
print("using newwisort: ",newwisort(nums))
print("using newwisort: ",newwisort([1,3,2,2,3,1]))
print("using newwisort: ",newwisort([1,5,1,1,6,4]))
print("using newwisort: ",newwisort([4,4,4,5,5,5]))
print("---------------------------------------")