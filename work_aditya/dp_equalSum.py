def subsetSum(wt, w):
    n=len(wt)
    t=[[False for i in range(w+1)] for i in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,w+1):
            if i==0:
                t[i][j]=False
            if j==0:
                t[i][j]=True
    for i in range(1, n+1):
        for j in range(1, w+1):
            if wt[i-1]<=j:
                t[i][j]= t[i-1][j-wt[i-1]] or t[i-1][j]
            else:
                t[i][j]= t[i-1][j]
    return t[n][w]

def equalSum(arr, n):
    summ=0
    for i in range(n):
        summ+= arr[i]
     
    if summ%2!=0:
        return False
    elif summ% 2==0:
        return subsetSum(arr, summ//2)


ls=[1,5,11,5]
n=len(ls)
print(equalSum(ls, n))
    
