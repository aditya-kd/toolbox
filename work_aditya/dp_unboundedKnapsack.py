#recursive
def unboundedKnapsack(wt, val, W, n):
    if W==0 or n==0:
        return 0
    if wt[n-1]>W:
        return unboundedKnapsack(wt, val, W, n-1)
    return max(unboundedKnapsack(wt, val, W, n-1), val[n-1]+unboundedKnapsack(wt, val,W-wt[n-1],n ))
#dp memoization
def unboundedKnapsackDP(wt, val, w, n, dp):
    if w==0 or n==0:
        dp[n][w]=0
    if dp[n][w]!=-1:
        return dp[n][w]
    if wt[n-1]>w:
        dp[n][w]=unboundedKnapsackDP(wt, val, w, n-1, dp)
        return dp[n][w]
    dp[n][w]= max(unboundedKnapsackDP(wt, val, w, n-1, dp), val[n-1]+unboundedKnapsackDP(wt, val, w-wt[n-1],n,dp))
    return dp[n][w]
#dp tabulation
def unboundedKnapsackTab(wt, val, w, n):#wrong output
    dp =  [[0]*(w+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, w+1):
            if wt[i-1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], val[i-1]+dp[i][j-wt[i-1]])
    return dp[n][w]
n=5
w=8
wt=[1,3,4,5,9]
val=[10,40,50,70,60]
dp=[[-1]*(w+1) for i in range(n+1)]
ans= unboundedKnapsackTab(wt, val, w, n)
# ans= unboundedKnapsack(wt, val, w, n)
# ans= unboundedKnapsackDP(wt, val, w, n, dp)
print(ans)

