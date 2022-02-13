def mergeSortedArr(arr1, m, arr2, n):

    for i in range(0,n):
        arr1[m+i]=(arr2[i])
    arr1.sort()
    return arr1

#second approach
def mergeSortedArr2(arr1, m, arr2, n):
    first=m-1
    second=n-1
    i=m+n-1
    while(second>-1):

        if arr1[first]<arr2[second]:
            arr1[i]=arr2[second]
            second-=1
            i-=1
        else:
            arr1[i]=arr1[first]
            first-=1
            i-=1
        

arr1=[1,3,5,0,0,0]
arr2=[2,4,6]
n=len(arr2)
#mergeSortedArr(arr1, 3, arr2, n)
mergeSortedArr2(arr1, 3, arr2, n)
print(arr1)
print(arr2)
            
