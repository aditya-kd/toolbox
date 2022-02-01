#lex_auth_01275171950687846476
def count_change(amount, coins):
    #start writing your code here
    m=len(coins)
    dp=[0]*(amount+1)
    dp[0]=1
    for i in range(0,m):
        j=coins[i]
        while j <= amount:
            dp[j]+= dp[j-coins[i]]
            j+=1
    return dp[amount]


print(count_change(200, [50, 25, 10, 5, 2, 1]))