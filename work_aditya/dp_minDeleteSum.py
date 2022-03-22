def f1(m, n, s1, s2, tbl):
    if tbl[m][n]==-1:
        if m==0 and n==0:tbl[m][n]=0
        elif m==0: 
            tbl[m][n] = f1(m, n-1, s1, s2, tbl)+ ord(s2[n-1])
        elif n==0:
            tbl[m][n]= f1(m-1, n, s1, s2, tbl)+ ord(s1[m-1])
        elif s1[m-1]==s2[n-1]: tbl[m][n] = f1(m-1, n-1, s1, s2, tbl)
        else:
            tbl[m][n] = min(f1(m-1, n, s1, s2, tbl)+ord(s1[m-1]),
            f1(m, n-1, s1, s2, tbl)+ ord(s2[n-1]))
        
    return tbl[m][n]

def minDeleteSum(s1, s2):
    tbl=[[-1](len(s2)+1) for i in range(len(s1)+2)]
    return f1(len(s1), len(s2), s1, s2, tbl)
