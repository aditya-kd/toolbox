def fibonacci(n):
    if n<=1: return n
    return fibonacci(n-1)+fibonacci(n-2)
dp=[0]*100
def fibdp(n):
    if n<=1: return n
    if dp[n]!=0 : return dp[n]
    dp[n]=fibdp(n-1)+fibdp(n-2)
    return dp[n]
def fibmemo(n):
    if n==0: return 0
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2, n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
num=10
for i in range(0,num):
    print(i,'th',fibmemo(i))