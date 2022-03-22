def findCeil(arr, num):
    l=0
    r=len(arr)-1
    while l<r:
        mid= (l+r)//2

        if arr[mid]==num:
            return mid
        elif arr[mid]< num:
            l= mid+1
        else:
            r=mid
    return l

arr=[1,5,7,9,12]
num=11
print(findCeil(arr, num))
