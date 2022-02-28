def mergeSorted(arr1, arr2):
    n1=len(arr1)
    n2=len(arr2)
    i=0
    j=0
    k=0
    arr3=[0]*(n1+n2)
    while i< n1 and j <n2:
        if arr1[i]<=arr2[j]:
            arr3[k]= arr1[i]
            i+=1
            k+=1
        else:
            arr3[k]=arr2[j]
            j+=1
            k+=1
    while i<n1:
        arr3[k]=arr1[i]
        i+=1
        k+=1
    while j<n2:
        arr3[k]= arr2[j]
        j+=1
        k+=1
    
    return arr3

def findMedian(test_list):
    mid=len(test_list)//2
    res= (test_list[mid] + test_list[~mid])/2
    return res


arr1=[1,2,3,7,8,9]
arr2=[4,5,6]
arr1=[1,2,3,4,5,6,7,8,9,10]
arr2=[11,12,13,14,15,16,16,18,19]
arr3=(mergeSorted(arr1, arr2))
print(arr3)
print("after merge finding median")
print(findMedian(arr3))


            