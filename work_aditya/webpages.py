def qwe(num,q3,confess, n, clicks, dest, page_list):
    for i in range(n):
        if clicks[num][i]==1:
            if i==dest:
                page_list.append(confess+1)
            clicks[num][i]=0
            qwe(i,q3,confess+1, n, clicks, dest, page_list)
            clicks[num][i]=1

page_list=[]
n=int(input())

clicks=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    query=list(map(int,input().split()))
    for j in query:
        clicks[i][j-1]=1
src,dest=map(int,input().split())
src-=1
dest-=1            
qwe(src,clicks,0, n, clicks, dest, page_list)
if len(page_list)==0:
    print(-1)
else:
    print(min(page_list))

