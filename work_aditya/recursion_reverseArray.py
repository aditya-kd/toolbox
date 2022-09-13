def reverseArr(arr, i, j):
    if i <= j:
        return arr
    arr[i], arr[j] = arr[j], arr[i]
    # i += 1
    # j -= 1
    # reverseArr(arr, i, j)
    return reverseArr(arr, i+1, j-1)

arr=[5,4,2,1]
reverseArr(arr, 0, len(arr)-1)
print(arr)