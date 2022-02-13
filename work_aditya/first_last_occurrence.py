def firstLastOccurrence(arr,k):
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
    first=ans
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
    last=ans
    print('First:', first, 'Last:',last)

    
arr=[1,2,3,4,4,5]
k=4
firstLastOccurrence(arr, k)
