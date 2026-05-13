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

def recwisort(arr,i=1):
    if i>=len(arr):# base case: this is the exit condition that happens (len(arr)) times [n]
        return arr
    # if statment is the main operation to check the [low, high] pattern and will happen (len(arr)) times [n]
    if ((i%2==0 and arr[i] > arr[i-1]) or#condition to check if the current element is in the correct order
        (i%2==1 and arr[i] < arr[i-1])):# based on its index (even or odd)
            arr[i],arr[i-1]=arr[i-1],arr[i]
    return recwisort(arr,i+1)# recursive call: moves to the next index, creating T(n-1) logic
#///////////////TEST
print("using recwisort: ",recwisort([1,3,2,2,3,1]))
print("using recwisort: ",recwisort([1,5,1,1,6,4]))
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
