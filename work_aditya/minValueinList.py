def minVal1(arr, n):
    minVal=0
    for i in range(0,n):
        for j in range(0,n):
            if arr[i]>arr[j]:
                minval=arr[j]
    print(minval)
    return minVal

def minVal(arr, n):
    minVal=(float('inf'))
    for i in range(0, n):
        if arr[i]<minVal:
            minVal=arr[i]
    print(minVal)
    return minVal

arr=[1,-9,12,45,675,245,886,2,-3]
minVal1(arr, len(arr))
minVal(arr,len(arr))

        
