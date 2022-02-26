import sys
n=0#number of houses
p=0#number of pipes
end=[0]*1100
dia=[0]*1100
start=[0]*1100
ans=0
def dfs(w):
    global ans
    if start[w]==0:
        return w
    if dia[w]<ans:
        ans=dia[w]
    return dfs(start[w])
  
def solve(arr):
    global ans
    i=0
    while i<p:
        q=arr[i][0]
        h=arr[i][1]
        t=arr[i][2]
        start[q]=h
        dia[q]=t
        end[h]=q
        i+=1
    
    result=[]
    for j in range(1, n+1):
        if end[j]==0 and start[j]:
            ans=1000000
            w=dfs(j)
            result.append([j, w, ans])
            
    print(result)
    
n=9
p=6
arr=[[7,4,98], [5,9,72],[4,6,10],[2,8,22],[9,7,17],[3,1,66]]
solve(arr)
