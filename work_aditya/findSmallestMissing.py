def bruteForce(arr):
    for i in range(len(arr)):
        if i!=arr[i]:
            return i
    return None

def binarySearch(arr):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]==mid:
            start=mid+1
        elif arr[mid]>mid:
            end=mid-1
        else:
            start=mid+1
        
    return start

arr=[0,1,2,3,5,6,7,8]
print(binarySearch(arr))

  