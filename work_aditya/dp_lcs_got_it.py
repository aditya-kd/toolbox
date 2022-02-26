#lcs recursive
def lcsrec(text1, text2, i, j):#complete length of t1 and t2
    if i<=0 or j<=0:
        return 0
    if text1[i-1]==text2[j-1]:
        return 1+lcsrec(text1, text2, i-1,j-1)
    else:
        return max(lcsrec(text1, text2, i-1,j), lcsrec(text1, text2, i,j-1))

#recursive with memoization solution
def lcsmem(text1, text2, i,j,dp):
    if i<=0 or j<=0:
        return 0
    if dp[i][j]!= -1:
        return dp[i][j]
    if text1[i-1] == text2[j-1]:
        return 1+ lcsmem(text1, text2, i-1, j-1,dp)
    else:
        dp[i][j]= max(lcsmem(text1, text2, i,j-1,dp), lcsmem(text1, text2, i-1, j, dp))
        return dp[i][j]
    
# This is a 2D solution can be further optimized
def longestCommonSubsequence(text1, text2):
    dp=[[0]*(len(text2)+1) for i in range(len(text1)+1)]
    for i in range(len(text1)-1, -1, -1):
        for j in range(len(text2)-1, -1, -1):
            if text1[i]==text2[j]:
                dp[i][j] = 1+ dp[i+1][j+1]
            else:
                dp[i][j]= max(dp[i][j+1], dp[i+1][j])
        
    return dp[0][0]

def lcs1D(text1, text2):
    dp=[0]*(len(text2)+1)
    for i in range(1, len(text1)+1):
        prev=0
        for j in range(1, len(text2)+1):
            temp = dp[j]
            if text1[i-1] == text2[j-1]:
                dp[j]= prev+1
            else:
                dp[j]=max(dp[j], dp[j-1])
            prev= temp
    return dp[len(text2)]

text1='AA'
text2='ABB'
# text1='SHINCHAN'
# text2='NOHARAAA'
# text1='ABCDEF'
# text2='FBDAMN'
dp=[[-1]*(len(text2)+1) for i in range(len(text1)+1)]
print(lcsrec(text1, text2, len(text1), len(text2)))