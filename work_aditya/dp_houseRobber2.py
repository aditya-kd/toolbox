def houseRobber2(nums):
    n=len(nums)
    if n==0: return 0
    if n==1: return nums[0]
    tbl=[0]*(n+1)
    tbl[0]=0
    tbl[1]=nums[0]
    for i in range(2, n):
        tbl[i]= tbl[i-2]+ nums[i-1]
        if tbl[i-1]>tbl[i]:
            tbl[i] = tbl[i-1]
    exluding=tbl[n-1]
    tbl[0]=0
    tbl[1]=0
    for i in range(2, n+1):
        tbl[i] = tbl[i-2]+nums[i-1]
        if tbl[i-1]> tbl[i]:
            tbl[i]= tbl[i-1]
    return max(tbl[n], exluding)