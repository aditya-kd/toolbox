def reverseArr(arr, i, j):
    if i>=j:
        return arr
    arr[i], arr[j] = arr[j], arr[i]
    arr = reverseArr(arr, i+1, j-1)
    return arr


arr = [5,4,2,1]
arr = reverseArr(arr, 0, len(arr)-1)
print(arr)