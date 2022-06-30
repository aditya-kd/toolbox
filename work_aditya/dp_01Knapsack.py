def ks01(wt, val, w, n):
    if n==0 or w==0:
        return 0
    if wt[n-1]<=w:
        return max(val[n-1]+ks01(wt, val, w-wt[n-1], n-1), ks01(wt, val, w, n-1))
    else:
        return ks01(wt, val, w, n-1)
def ks(wt, val,w, n):
    t = [[0 for x in range(w + 1)] for x in range(n + 1)]
  
    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
                
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if wt[i-1] <= j:
                t[i][j] = max(val[i-1] + t[i-1][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
 
    return t[n][w]
 
 
# Driver code
val = [60, 100, 120]
wt = [10, 20, 30]
w = 50

    
# wt=[1,3,4,5]
# val=[1,4,5,2]
# val=[1,2,3]
# wt=[4,5,1]
# w=4
# val=[60,100,120]
# wt=[10,20,30]
# w=50
print(ks01(wt, val, w, len(wt)))