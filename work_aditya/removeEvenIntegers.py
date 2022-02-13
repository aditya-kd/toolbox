#replacing even with 0
def removeEven(arr,n):
    for i in range(n):
        if arr[i]%2==0:
            arr[i]=0.0
    arr
#storing only odd elements in a new array
def removeEven2(arr, n):
    res=[]
    for i in range(n):
        if arr[i]%2==0:
            continue
        res.append(arr[i])
    return res
#using pointer m to fill odd numbers first
def removeEven3(arr, n):
    m=0
    for i in range(n):
        if arr[i]%2!=0:
            arr[m]=arr[i]
            m+=1
        
    for i in range(m,n):
        arr[i]=0

    print(arr)

arr=[1,2,3,4,5,6,6,7]
n=len(arr)
removeEven(arr, n)


