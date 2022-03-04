def solve(s):
    mp={}
    start=0
    end=0
    ans=0
    while end<len(s):
        if s[end] in mp:
            ans= max(ans , end-start+1)
            start = mp[s[end]]+1
        else:
            ans=max(ans, end-start+1)
            mp[s[end]]=end
        end+=1

    return ans


instr='abcbb'
print(solve(instr))

    

