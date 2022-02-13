def maxSuminArr(arr ):
    cursum= arr[0]
    overall= arr[0]
    for i in range(1, len(arr)):
        if cursum >=0:
            cursum +=arr[i]
        else:
            cursum = arr[i]

        if cursum > overall:
            overall = cursum
        
    return overall

def maxSumSubArr(arr):
    pass
    