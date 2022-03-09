def rodCutting(wt, val, w, n):
    dp =  [[0]*(w+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, w+1):
            if wt[i-1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                #val[n-1] is different from original unbounded
                dp[i][j] = max(dp[i-1][j], val[n-1]+dp[i][j-wt[i-1]])
    return dp[n][w]

w=6
pieces=[i for i in range(1, w+1)]
print(pieces)
prices=[10,40,60,20,30,20]
ans=rodCutting(pieces, prices, w, w)
print(ans)




