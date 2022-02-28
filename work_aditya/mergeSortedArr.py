def mergeSortedArr(arr1, m, arr2, n):
    for i in range(0,n):
        arr1[m+i]=(arr2[i])
    arr1.sort()
    return arr1
#using extra array arr3 This one is legit correct
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

#second approach this one is for merging in those arrays only
def mergeSortedArr2(arr1, m, arr2, n):
    last= m+n -1
    while m>0 and n> 0:
        if arr1[m-1] > arr2[n-1]:
            arr1[last] = arr1[m-1]
            m-=1
        else:
            arr1[last]=arr2[n-1]
            n-=1
        last-=1
    while n>0:
        arr1[last]= arr2[n-1]
        n, last= n-1, last-1


arr1=[1,3,5,0,0,0]
arr2=[2,4,6]
n=len(arr2)
#mergeSortedArr(arr1, 3, arr2, n)
mergeSortedArr2(arr1, 3, arr2, n)
print(arr1)
print(arr2)
            
