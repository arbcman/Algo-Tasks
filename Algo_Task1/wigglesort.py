
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

