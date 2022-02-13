def binarySearch(arr, k):
    ans=-1
    beg=0
    end=len(arr)-1
    while(beg<=end):
        mid=(beg+end)//2
        if arr[mid]==k:
            ans=mid
            beg=mid+1
        elif arr[mid]<k:
            beg=mid+1
        else:
            end=mid-1
    return ans

arr=[1,2,3,4,4,5]
k=4
print(binarySearch(arr, k))
