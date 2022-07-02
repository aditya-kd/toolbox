def merge(arr, l, m, r):
    n1 = m-l+1
    n2 = r-m
    left=[0]*n1
    right=[0]*n2
    for i in range(n1):
        left[i] = arr[l+i]
    for j in range(n2):
        right[j]= arr[m+j+1]
    i=0
    j=0
    k=l
    while i<n1 and j<n2:
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    while i < n1:
        arr[k]= left[i]
        i+=1
        k+=1
    while j<n2:
        arr[k]= right[j]
        j+=1
        k+=1
def mergesort(arr, l, r):
    if l<r:
        m=l+(r-l)//2
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
        merge(arr, l, m,r)
        print("Pass",arr)


arr=[78,-90,45,23,34,11,12]
n= len(arr)
mergesort(arr, 0, n-1)
print(arr)
    