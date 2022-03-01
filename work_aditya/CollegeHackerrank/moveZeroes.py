

def zero(arr):
    c=0
    n=len(arr)
    for i in range(0, len(arr)):
        if arr[i]!=0:
            arr[c]=arr[i]
            c+=1
    i=c
    while i<n:
        arr[i]=0
        i+=1

    print(arr)


arr=[1,0,4,0,6]
zero(arr)