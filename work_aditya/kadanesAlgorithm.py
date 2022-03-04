def maxSubArr(arr):
    curSum=arr[0]
    overall=arr[0]

    for i in range(1, len(arr)):
        if curSum >=0:
            curSum +=arr[i]
        else:
            curSum=arr[i]
        if curSum>overall:
            overall=curSum
    return overall


ls=[-2, -3, -4, -1, 2, -1, -3]
print(maxSubArr(ls))


