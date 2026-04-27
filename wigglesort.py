def wisort(arr):
    for i in range(1,len(arr)):
        if ((i%2==0 and arr[i] > arr[i-1]) or
        (i%2==1 and arr[i] < arr[i-1])):
            arr[i],arr[i-1]=arr[i-1],arr[i]
    return arr
def reqwisort(arr,i=1):
    if i>=len(arr):
        return arr
    if ((i%2==0 and arr[i] > arr[i-1]) or
        (i%2==1 and arr[i] < arr[i-1])):
            arr[i],arr[i-1]=arr[i-1],arr[i]
    return reqwisort(arr,i+1)


print(wisort([1,3,2,2,3,1]))
print(wisort([1,5,1,1,6,4]))
print(reqwisort([1,3,2,2,3,1]))
print(reqwisort([1,5,1,1,6,4]))