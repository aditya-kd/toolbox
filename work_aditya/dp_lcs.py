def lcsFinal(str1, str2, m, n):
    dp = [[0]*(n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

def lcs2(str1, str2, m, n, dp):
    if m==0 or n==0:
        return 0
    if dp[m][n]!=-1:
        if str1[m-1] ==  str2[n-1]:
            dp[m][n] = 1+lcs2(str1, str2, m-1, n-1)
            return dp[m][n]
    dp[m][n]= max(lcs2(str1, str2, m, n-1, dp), lcs2(str1, str2, m-1, n, dp))
    return dp[m][n]


str1='a'
str2='a'
m=len(str1)
n=len(str2)
print(lcsFinal(str1, str2, m, n))