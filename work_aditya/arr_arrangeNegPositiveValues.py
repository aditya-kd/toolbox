
#using sorting the array -ve to the left, +ve to right
def merge(arr, l, m, r):
    #create both arrays
    n1=m-l+1
    n2=r-m
    left=[0]*n1
    right=[0]*n2
    #fill both arrays
    for i in range(0, n1):
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
            j+=1
        k+=1
    while i<n1:
        arr[k]=left[i]
        i+=1
        k+=1
    while j<n2:
        arr[k]=right[j]
        j+=1
        k+=1
    
def mergesort(arr,l, r):
    if l<r:
        m=l+(r-l)//2
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
        merge(arr, l, m, r)

def arrange1(arr):
    n=len(arr)
    mergesort(arr, 0, n-1)
    return arr

#second approach taking two pointers on each side
def arrange2(arr):
    i=0
    j=len(arr)-1
    while(i<j):
        if arr[j]>=0:
            j-=1
        if arr[i]<0 and arr[j]<0:
            j-=1
        if arr[i]>=0 and arr[j]<0:
            arr[i],arr[j]=arr[j],arr[i]
    print(arr)
    
arr=[7,-3,4,8,-9,-1,18]
print(arrange1(arr))
arrange2(arr)
    
    
