def maxSubArr(arr, k):
    size=0
    #store overall result
    res = 0
    #find the sum till 0 to k-1
    while size <= k-1 :
        res += arr[size]
        size += 1
    
    print(res)
    currsum = res
    
    #iterate on the array from k+1 size
    for i in range(k, len(arr)):

        if currsum < currsum+arr[i]:
            print(currsum, res, currsum+arr[i])
            currsum = currsum+arr[i]
            res = currsum
    
    for i in range(k, len(arr)):

        if currsum>=0:
            cursum += arr[i] 
            res.append(arr[i])
        
        
    


        






arr=[-4,-2,1,-3]
k=2
maxSubArr(arr, k)