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
    cursum= arr[0]
    overallsum=arr[0]
    start=0
    end=0
    maxarr=[]
    maxarr.append(arr[0])
    for i in range(1, len(arr)):
        if cursum>=0:
            cursum += arr[i]
            maxarr.append(arr[i])
            end=i
        else:
            cursum= arr[i]
            maxarr=[]
            maxarr.append(arr[i])
            start=i
        if overallsum< cursum: 
            overallsum = cursum
            print('Current:',start, end)
            print('Current ans', maxarr)
    

ls=[-2, -3, 4, -1, 2, 1, -3]
maxSumSubArr(ls)

    