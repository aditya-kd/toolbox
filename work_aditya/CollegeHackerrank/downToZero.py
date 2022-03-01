max=1000001
nums=[-1]*max

nums[0]=0
nums[1]=1
nums[2]=2
nums[3]=3

for i in range(0,max):
    if nums[i]==-1 or nums[i]>(nums[i-1]+1):
        nums[i] = nums[i-1]+1
    j=1
    while j<=i and (j*i)<max :
        if nums[j*i] == -1 or (nums[i]+1) <nums[j*i]:
            nums[j*i] = nums[i]+1

q=int(input())
for i in range(q):
    n=int(input())
    print(nums[n])


n=10000



import math
n=1000001
dp =[float('inf')]*n
dp[0]=0
dp[1]=1
for i in range(2, n):
    dp[i]= min(dp[i], dp[i-1]+1)
    sqr= int(math.sqrt(i))
    for j in range(2, sqr+1):
        if i%j==0:
            dp[i]=min(dp[i], dp[i/j]+1)

q=int(input())
for i in range(0,q):
    n=int(input())
    print(dp[n])


