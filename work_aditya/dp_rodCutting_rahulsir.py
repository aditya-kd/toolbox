from cmath import inf
from tokenize import ContStr

import sys
def solve(n, prices:list):
    if n==0: return 0
    maxlen=-sys.maxsize
    cost=0
    for i in range(1, n+1):
        cost += max(  prices[i-1], solve(n-1, prices))
        if cost>maxlen:
            maxlen=cost
    return maxlen

def solve2(n, prices):
    dp=[-1 for i in range(n+1)]
    dp[0]=0
    dp[1]=prices[0]
    for i in range(2, n+1):
        for j in range(1,i+1):
            dp[i] = max(dp[i], prices[j-1] + dp[i+j])

    return dp[n]
p=[2,5,8,9,10,17,17,20]
l=[i for i in range(1, len())]
# prices=[10,20,30,40]
n=4
print(solve(n, p))