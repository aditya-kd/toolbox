def binarySearch(arr, k):
    beg=0
    end=len(arr)-1
    ans=-1
    while(beg<=end):
        mid=(beg+end)//2
        if arr[mid]==k:
            ans=mid
            end=mid-1
        elif arr[mid]>k:
            end=mid-1
        else:
            beg=mid+1
    return ans

arr=[0,1,2,3,3,4,5]
k=3
print(binarySearch(arr, k))
