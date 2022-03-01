def subset(arr, k):
    mp=[0]*(k)
    for i in arr:
        mp[i%k]+=1
    print(mp)
    ans=0
    if mp[0]>0:
        ans+=1
    
    for i in range(1, k):
        if mp[i]==0: continue

        if (2*i ==k):
            ans+=1
        else:
            ans+=max(mp[i], mp[k-i])
            mp[i]=0
            mp[k-i]=0
    print(ans)
    return ans
arr=[1, 7, 2, 4]
k=3
subset(arr, 3)
    