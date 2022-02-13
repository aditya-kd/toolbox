def binarySearch(arr,start, end , k):
    if start>end:
        print(k,'not found')
        return -1
    else:
        m=(start+end)//2
        if arr[m]==k:
            print('Found at',m)
            return m
        elif arr[m]>k:
            binarySearch(arr, start, m-1, k)
        else:
            binarySearch(arr, m+1, end, k)
    
arr=[-1,0,3,5,9,12]
k=10
binarySearch(arr, 0, len(arr)-1, k)
   