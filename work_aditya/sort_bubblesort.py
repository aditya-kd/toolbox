def bubbleSort(arr, n):

    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
        print('Pass',i+1, arr)
    return arr
    
arr=[34,25,6,7,12,89,-90]
n=len(arr)
print(bubbleSort(arr, n))
