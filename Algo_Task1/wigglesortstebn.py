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
print("using newwisort: ",newwisort([1,3,2,2,3,1]))
print("using newwisort: ",newwisort([1,5,1,1,6,4]))
print("using newwisort: ",newwisort([4,4,4,5,5,5]))
print("---------------------------------------")
print("---------------------------------------")
print("merge_sort then Recursive wiggle Implementation:")

def recnewwisort(nums, first_call=True):
    if len(nums) <= 1:
        return nums
    # first iteration check (to sort the array)
    if first_call:
        nums = merge_sort(nums)
    n = len(nums)
    mid = n // 2
    # split and reverse halves
    left = nums[:mid][::-1]
    right = nums[mid:][::-1]
    # if one side is empty we will just return the other 
    if not left:
        return right
    if not right:
        return left
    # take first elements then recurse on the rest
    return [left[0], right[0]] + recnewwisort(left[1:] + right[1:], first_call=False)

print("using recnewwisort: ",recnewwisort([1,3,2,2,3,1]))
print("using recnewwisort: ",recnewwisort([1,5,1,1,6,4]))
print("using recnewwisort: ",recnewwisort([4,4,4,5,5,5]))
print("---------------------------------------")
print("---------------------------------------")
print(__name__)