import sys

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
    # return dp[n][summ]
    vector=[]
    for i in range( len(dp[n])//2 ):
        if dp[n][i]==True:
            vector.append(i)
    minm=sys.maxsize
    for i in range(len(vector)):

        minm= min(minm, abs(summ- (2*vector[i])))
    print(minm)
    return minm
    
    


arr=[1,2,7]
n=len(arr)
ss=sum(arr)
subsetSum(arr, n, ss)
