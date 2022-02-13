def maxProductSubarray(arr):
    res=max(arr)
    curMin, curMax= 1,1
    for n in arr:
        if n==0:
            curMin, curMax=1,1
            continue
        temp=curMax*n
        curMax=max(n*curMax, n*curMin, n)
        curMin=min(temp, n*curMin, n)
        res=max(res, curMax)

    return res

arr=[6,-3,-10,0,2]
print(maxProductSubarray(arr))
