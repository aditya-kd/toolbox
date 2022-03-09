def solve(arr):
    forward=[]
    bkwd=[]
    #forward kadanes 
    curSum=0
    # osum=arr[0]
    for i in range(0, len(arr)):
        if curSum >=0:
            curSum +=arr[i]
        else:
            curSum=arr[i]
        forward.append(curSum)
    print(forward)
    curSum=0
    for i in range(len(arr)-1, -1, -1):
        if curSum>=0:
            curSum+=arr[i]
        else:
            curSum=arr[i]
        bkwd.append(curSum)
    bkwd.reverse()
    print(bkwd)
    ans=max(forward)

    for i in range(0,len(arr)-2):
        # print(forward[i]+bkwd[i+2])
        ans=max(ans, forward[i]+bkwd[i+2])
    print(ans)
    return ans
    

arr=[1,-2,0,3]
arr=[1,-2,-2,3]
solve(arr)

