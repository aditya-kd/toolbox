def subsetSum(arr, n ,summ):
    dp= [[False]*(summ+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1, n+1):
        for j in range(1, summ+1):
            if arr[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
    return dp[n][summ]
def subsetSumRecur(arr, n, k):
    if k==0: return True
    if k<0 or n==0: return False
    include= subsetSumRecur(arr, n-1, k-arr[-1])
    execlude = subsetSumRecur(arr, n-1, k)
    return include or execlude

arr=[3,4,6,2]
n=4
summ=9
ans=subsetSum(arr, n, summ)
print(ans)
print(subsetSumRecur(arr, n, summ))
