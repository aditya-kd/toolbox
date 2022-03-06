def countSubsetSum(wt, w, n):
    t=[[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(0, n+1):
        for j in range(0, w+1):
            if i==0:
                t[i][j]=0
            if j==0:
                t[i][j]=1
        
    for i in range(1, n+1):
        for j in range(w+1):
            if wt[i-1]<=j:
                t[i][j]= t[i-1][j-wt[i-1]]+t[i-1][j]
            else:
                t[i][j]= t[i-1][j]
            
    return t[n][w]


ls=[2,3,5,6,8,10]
ls=[1,2,3,4,5]
ls=[3,3,3,3]
ls=[3,4,4,1]
s=10
s=10
s=0
print(countSubsetSum(ls, s, len(ls)))
    