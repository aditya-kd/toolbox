
def removeDuplicate(arr):
    arr.sort()
    print(arr)
    n=len(arr)
    k=1
    for i in range(1, n):
        if arr[i-1]!= arr[i]:
            arr[k]=arr[i]
            k+=1
    print(arr[0:k])
    return arr[0:k]

ls=[1,2,3,1,4,5,1,5,2,1]
removeDuplicate(ls)