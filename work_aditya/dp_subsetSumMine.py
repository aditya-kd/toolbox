def subsetSum(wt, w, n):
    t=[[False for i in range(w+1)] for x in range(n+1)]

    for i in range(0, n+1):
        for j in range(0,w+1):
            if i==0:
                t[i][j]=False
            if j==0:
                t[i][j]=True
    print(t)
    for i in range(1, n+1):
        for j in range(1, w+1):
            if wt[i-1]<=j:
                t[i][j]= t[i-1][j-wt[i-1]] or t[i-1][j]
            else:
                t[i][j]= t[i-1][j]

    return (t[n][w])



wt=[2,3,8]
w=11
wt=[3,34,4,12,5,2]
w=30

print(subsetSum(wt, w, len(wt)))