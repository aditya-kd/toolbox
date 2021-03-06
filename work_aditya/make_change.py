def make_change(denomination_list, amount):
    denomination_list.sort(reverse=True)
    i=0
    cnt=0
    while amount>0 and i<len(denomination_list):
        if (amount //denomination_list[i])>=0:
            x=(amount//denomination_list[i])
            cnt+=x
            amount-=(x*denomination_list[i])

        i+=1
    if cnt==0:
        return -1

def coin_change_main(amount, coins):
    dp=[0]*(amount+1)
    dp[0]=1
    for i in range(0,len(coins)):
        coin=coins[i]
        for j in range(coin, len(dp)):
            dp[j] += dp[j-coin]
    return dp[amount]


#lex_auth_01275171950687846476
def count_change(amount, coins):
    #start writing your code here
    if amount==0:
        return 1
    if amount<0:
        return 0
        
    if len(coins)<=0 and amount>=1:
        return 0
        
    return count_change( coins[0:len(coins)-1], amount) + count_change(coins, amount-coins[-1])

def count_change_2d(amount, coins):

    dp=[ [0]*(amount+1) for i in range(len(coins))]
    for i in range(len(coins)):
        dp[i][0]=1

    for i in range(0, len(coins)):
        for j in range(1, amount+1):
            if j< coins[i]:
                if i>0:
                    dp[i][j]=dp[i-1][j]
            else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-coins[i]]
    return dp[len(coins)-1][amount]

print(count_change_2d(5, [50, 25, 10, 5, 2, 1]))
# print(count_change_akashsir(5, [1,2,5]))

        
