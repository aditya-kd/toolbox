def LIS(arr):
    omax=0
    n=len(arr)
    dp=[0]*(len(arr))
    for i in range(n):
        mxm= 0
        for j in range(i):
            if arr[j] < arr[i]:
                if dp[j] >mxm:
                    mxm = dp[j]
        dp[i] = mxm+1
        if dp[i] >omax:
            omax=dp[i]
    print(omax)
    print(dp)

ls=[10,22,9,33,21,50,41,60,80,3]
ls=[21,4,2,16,17,3,13,14]
LIS(ls)
