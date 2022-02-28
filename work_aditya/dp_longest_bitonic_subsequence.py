def LIS(arr):
    n=len(arr)
    dp=[0]*n
    for i in range(n):
        mxm= 0
        for j in range(i):
            if arr[j]<arr[i]:
                if dp[j]>mxm:
                    mxm=dp[j]
        dp[i]=mxm+1

    return dp
#LDS
def LDS(arr):
    n=len(arr)
    dp=[0]*n
    for i in range(n-1,-1,-1):
        mxm=0
        for j in range(n-1, i-1,-1):
            if arr[j]<arr[i]:
                if dp[j]>mxm:
                    mxm=dp[j]
        dp[i] = mxm+1
        
    return dp

def LBS(arr):
    lis=LIS(arr)
    lds=LDS(arr)
    print(lis)
    print(lds)
    omax=0
    for i in range(len(arr)):
        if lis[i]+lds[i]-1> omax:
            omax= lis[i] + lds[i]-1
    print(omax)

ls=[10,22,9,33,21,50,41,60,80,3]
ls=[1,2,5,3,2]
LBS(ls)


