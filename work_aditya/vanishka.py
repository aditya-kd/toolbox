def valueofFriends(n, queryType, student1, student2):
    fr,h=[],[]
    def pre(x): 
        global fr
        if x!=fr[x]: fr[x]=pre(fr[x])
        return fr[x]

    def union(x,y):
        global fr,h
        x,y=pre(x),pre(y)
        if x!=y:
            if h[x]<h[y]: x,y=y,x
            fr[y]=x
            if h[x]==h[y]: h[x]+=1
                
    def calc():
        cnt={}
        global fr,h
        n,m=map(int,input().split())
        fr,h=list(range(n)),[0]*n
        for i in range(len(student1)):
            x = student1[i]
            y= student2[i]
        
            union(x-1,y-1)
        for t in range(n): fr[t]=pre(t)    
        for i in range(n): cnt[fr[i]]=cnt.setdefault(fr[i],0)+1
        total,cur,ans=0,0,sorted([cnt[key] for key in cnt if cnt[key]>1],reverse=True)
        for x in ans:
            for i in range(2,x+1):
                cur+=i*2-2
                total+=cur
        print(total+cur*(m-sum(ans)+len(ans)))

    for _ in range(int(input())): calc()