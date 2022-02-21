import sys
def rmcm(arr, i, j):
    if i==j: return 0
    minmum=sys.maxsize
    for k in range(i,j):
        count = rmcm(arr, i,k)+ rmcm(arr, k+1,j)+arr[i-1]*arr[k]*arr[j]
        if count< minmum:
            minmum=count
    return minmum

def mcm(arr, n):
    return rmcm(arr, 1, n-1)

# import sys
# def rmcm(arr, i, j,dp):
#     minimum=sys.maxsize
#     if i==j: 
#         dp[i][j]=0
        

#     if dp[i][j]!=-1:
#         return dp[i][j]
#     for k in range(i,j):
#         count = rmcm(arr, i,k, dp)+ rmcm(arr, k+1,j, dp)+arr[i-1]*arr[k]*arr[j]
#         if count< minimum:
#             minimum=count
#     dp[i][j]=minimum
#     return dp[i][j]

# def mcm(arr, n):
#     dp =[[-1]*(n) for i in range(n)]
#     return rmcm(arr, 1, n-1, dp)

ls=[2,3,4,3,5]
n=len(ls)
print(mcm(ls, n))