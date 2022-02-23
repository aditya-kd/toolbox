import math


n=0#houses
p=0#pipes
rd=[0]*1100#start of pipe
wt=[0]*1100#diameter of pipe
cd=[0]*1100#end of pipes

a=[]
b=[]
c=[]
ans=0
def dfs(w):
    global ans
    if cd[w]==0: return w
    if wt[w]<ans: ans= wt[w]
    return dfs(cd[w])

def waterConnection(arr):
    global ans
    i=0
    while i<p:
        q=arr[i][0]
        h=arr[i][1]
        t=arr[i][2]

        cd[q]=h #add end of pipe
        wt[q]=t #diameter
        rd[h]=q #add start making it connected on both sides

    a=[]
    b=[]
    c=[]
    for j in range(1, n+1):
        if rd[j] ==0 and cd[j]: #outgoind pipe
            ans= math.inf

            w=dfs(j)

            a.append(j)
            b.append(w)
            c.append(ans)
    print(len(a))
    for j in range(len(a)):
        print(a[j], b[j], c[j])

n= 9
p=6
arr = [[7, 4, 98], [5, 9, 72], [4, 6, 10 ],
        [2, 8, 22 ], [9, 7, 17], [3, 1, 66]]
waterConnection(arr)



