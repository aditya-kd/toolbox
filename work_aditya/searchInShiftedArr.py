def binarySearch(arr, n, target):
    beg=0
    end=n-1
    while(beg<end):
        mid=(beg+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            beg=mid+1
        else:
            end=mid-1
    return -1
def findElement(arr, n, target):
    #find break point
    beg=0
    end=n-1
    last=arr[n-1]
    while(beg<end):
        mid=(beg+end)//2
        if arr[mid-1]>arr[mid] and arr[mid]<arr[mid+1]:
            breakindex=mid
            break
        if arr[mid]<last:
            beg=0
            end=mid-1
        elif arr[mid]>last:
            end=mid-1

    search1=binarySearch(arr[0:breakindex], n, target)
    search2=binarySearch(arr[breakindex:], n, target)

    print(search1, search2) 



ls=[15,18,20,3,5,6,12]
n=len(ls)
print(findElement(ls, n, 3))


    

    
            
        