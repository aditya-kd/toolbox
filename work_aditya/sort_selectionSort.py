def selectionsort(arr, n):

    for i in range(0, n-1):
        pos=i
        for j in range(i+1, n-1):
            if arr[pos] > arr[j]:
                pos = j
        arr[i], arr[pos] = arr[pos], arr[i]
        print('Pos:',pos,'Pass',i+1, arr)

    return arr

arr=[34,25,6,7,12,89,-90]
n=len(arr)
print(selectionsort(arr, n))
    



