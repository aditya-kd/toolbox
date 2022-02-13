def findFirstOccurrence(arr, n, target):
    for i in range(0, n):
        if arr[i]==target:
            return i

def findFirstOccurrence2(arr, n, target):
    start=0
    end=n-1
    ans=0
    while(start<=end):
        m=(start+end)//2
        if arr[m]==target:
            ans=m
            end=m-1
        elif arr[m]>target:
            end=m-1
        else:
            start=m+1
    return ans
arr=[3,10,11,15,17,17,17,20]
n=len(arr)
target=17
print(findFirstOccurrence(arr, n, target))

        
