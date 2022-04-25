def lcs(s1, s2, n, m):
    n=len(s1)
    m=len(s2)
    if n==0 or m==0:
        return 0
    if s1[n-1]==s2[m-1]:
        return 1+lcs(s1, s2, n-1, m-1)
    else:
        return max(lcs(s1, s2, n-1, m),
        lcs(s1,s2, n, m-1))

def lcs2(s1, s2, n, m, qb):
    if n==0 or m==0:return 0
    if qb[n][m]!=0:
        return qb[n][m]
    if s1[n-1]==s2[m-1]:
        return 1+lcs(s1, s2, n-1, m-1)
    else:
        qb[n][m]=max(lcs(s1, s2, n-1, m), 
        lcs(s1, s2, n, m-1))
        return qb[n][m]

def lcs(s1, s2, n, m):
    dp=[n+1][m+1]
    for i in range(0,n):
        for j in range(0,m):
            if i==0 or j==0:
                dp[i][j]=0
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j], dp[i][j-1])

# s1='SINCHAN'
# s2='NOHARAA'
# qb=[[0]*(len(s1)+1) for i in range(len(s2)+1)]
# print(lcs2(s1, s2, len(s1), len(s2), qb))

s1='Aditya'
s2='Adya'
lcs(s1, s2, len(s1),len(s2))
