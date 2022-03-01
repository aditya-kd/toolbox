def abbreviation(a, b):
    # Write your code here
    qb=[[0]*(len(a)+1) for i in range(len(b)+1)]
    qb[0][0]=1
    for i in range(1, len(b)+1):
        for j in range(1, len(a)+1):
            if a[j-1].islower():
                if a[i-1] == b[j-1] and qb[j-1][i-1]:
                    qb[j][i]=1
            else:
                if (a[i-1]).upper() == qb[j-1] and qb[j-1][i-1]==1:
                    qb[j][i]=1
                else:
                    qb[j][i] = qb[j][i-1]
                    
    if qb[len(b)][len(a)] ==1:
        return "YES"
    else:
        return "NO"

def abbreviation(a, b):
    m, n = len(a), len(b)
    dp = [[False]*(m+1) for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 and j != 0:
                dp[i][j] = a[j-1].islower() and dp[i][j-1]
            elif i != 0 and j != 0:
                if a[j-1] == b[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif a[j-1].upper() == b[i-1]:
                    dp[i][j] = dp[i-1][j-1] or dp[i][j-1]
                elif not (a[j-1].isupper() and b[i-1].isupper()):
                    dp[i][j] = dp[i][j-1]
    return "YES" if dp[n][m] else "NO"     
    


a='AbcDE'
b='ABDE'
