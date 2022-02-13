def pairs(k, arr):
    # Write your code here
    arr.sort()
    i=0
    j=1
    total=0
    while(j<len(arr)):
        diff=arr[j]-arr[i]
        if diff==k:
            total+=1
            j+=1
        elif diff>k:
            i+=1
        elif diff<k:
            j+=1
    return total

arr=[7,8,5,6,2,-1]
k=11
print(pairs(k, arr))
