def binarySearch(arr, k):
    beg=0
    end=len(arr)-1
    while(beg<=end):
        mid=(beg+end)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]>k:
            end=mid-1
        else:
            beg=mid+1
    return -1

arr=[1,2,3,3,4,5]
k=1
print(binarySearch(arr, 1))
