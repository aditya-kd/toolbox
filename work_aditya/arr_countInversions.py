def countInversions1(arr):
    inverts=0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                inverts+=1
    return inverts

def merge(arr, l, m ,r):
    n1=m-l+1
    n2=r-m
    left=[0]*n1
    right=[0]*n2
    inv=0
    #fill left array
    for i in range(0,n1):
        left[i]=arr[l+i]

    for j in range(0, n2):
        right[j]=arr[m+1+j]

    i,j,k=0,0,l
    while i<n1 and j<n2:
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            inv+= m-i+1
            j+=1
        k+=1
    while(i<n1):
        arr[k]=left[i]
        i+=1
        k+=1
    while(j<n2):
        arr[k]=right[j]
        j+=1
        k+=1
    
    return inv


def mergeSort(arr, l, r):
    inv=0
    i=0
    if l<r:
        m=l+(r-l)//2
        inv+=mergeSort(arr, l, m)
        inv+=mergeSort(arr, m+1, r)
        inv+=merge(arr, l, m, r)
    return inv
    
def countInversions2(arr):
    return (mergeSort(arr, 0, len(arr)-1))
    

arr=[3,2,1]
print(countInversions1(arr))
print(countInversions2(arr))


