from itertools import count
def countDerangement(n):
    if n==1:#no possiblity
        return 0
    if n==2:#[A, B] only one possiblity [B,A]
        return 1
    return (n-1)* (countDerangement(n-2) + countDerangement(n-1))

def countDerangement2(n):#Using DP storing results for prev.
    dp=[0]*(n+1)
    dp[1]= 0
    dp[2]= 1
    for i in range(3, n+1):
        dp[i] = (i-1)* (dp[i-1] + dp[i-2])
    
    # print(dp[n])
    return dp[n]

n=3
print(countDerangement(n))
print(countDerangement2(n))

    