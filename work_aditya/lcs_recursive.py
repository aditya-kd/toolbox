def lcs(str1, str2, m , n):
    if m==0 or n==0:
        return 0
    
    if str1[m-1] == str2[n-1]:
        return 1+lcs(str1, str2, m-1, n-1)
    
    return max(lcs(str1, str2, m, n-1), lcs(str1, str2, m-1, n))
# def lcsdp(str1, str2, m, n, dp):
#     if m==0 or n==0:
#         return 0
#     if dp[m][n]!=-1:
#         return dp[m][n]
#     if str1[m-1] == str2[n-1]:
#         dp[m][n]= 1+lcsdp(str1, str2, m-1, n-1, dp)
#         return dp[m][n]
#     dp[m][n] = max(lcsdp(str1, str2, m, n-1, dp), lcs(str1, str2, m-1, n,dp))
#     return dp[m][n]

if __name__ == '__main__':
    str1='a'
    str2='a'
    m= len(str1)
    n=len(str2)
    # dp = [[-1]*(m+1) for i in range(n+1)]
    # for i in range(m+1):
    #     for j in range(n+1):
    #         if i==0 or j==0:
    #             dp[i][j] =0
    # ans=lcs(str1, str2, m, n, dp)
    ans=lcs(str1, str2, m, n)
    print(ans)

