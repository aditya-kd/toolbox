def solve(p):
    f=[0]*1024
    for i in range(0, len(p)):
        x=p[i]
        mask=0
        for j in range(0, len(x)):
            number= ord(x[i]) - ord('0')
            mask |= (1<<number)
        f[mask]+=1
    
    ans=0
    for i in range(0, 1024):
        for j in range(i, 1024):
            if i|j==1024:
                if i==j:
                    ans+=(f[i]+(f[j]-1))//2
                else:
                    ans+=f[i]*f[j]
    return ans

