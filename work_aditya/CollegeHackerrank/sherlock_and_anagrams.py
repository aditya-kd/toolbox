#brute force used since constraint was small
#len<=100
def sherlockAndAnagrams(ls):
    # Write your code here
    mp={}
    n=len(ls)
    s=list(ls)
    for i in range(1, n):
        for j in range(i+1, n-i ): 
            t=s[j:i]
            mp[str(t)]=mp.get(str(t), 0)+1
    res=0
    for item in mp.keys():
        res+= (mp[item]*(mp[item]-1))//2
    return res