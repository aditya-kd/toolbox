def LIS(arr):
    omax=0
    n=len(arr)
    dp=[0]*(len(arr))
    # for i in range(n):
    for i in range(n-1, -1,-1):
        mxm= 0
        # for j in range(i):
        for j in range(i, -1,-1):
            if arr[j] < arr[i]:
                if dp[j] >mxm:
                    mxm = dp[j]
        dp[i] = mxm+1
        if dp[i] >omax:
            omax=dp[i]
    print(omax)

ls=[10,22,9,33,21,50,41,60,80,3]
LIS(ls)
