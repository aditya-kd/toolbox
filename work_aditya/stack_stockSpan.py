def minSpan(arr):
    n=len(arr)
    s=[]
    v=[]
    span=[]
    for i in range(n):
        while len(s)>0 and  s[-1][0]<=arr[i]:
            s.pop()

        if len(s)==0:
            v.append(-1)
            # v[i]=-1
        
        else:
            v.append(s[-1][1])
            # v[i]=s[-1][1]

        s.append([arr[i],i])

    for i in range(n):
        span.append(i-v[i])
    return span
