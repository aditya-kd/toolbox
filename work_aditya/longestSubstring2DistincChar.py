def longestSubstr1(instr):
    if len(instr)<3: return len(instr)
    left=0
    right=0
    mp={}
    anslen=0

    size=len(mp)
    while right<len(instr):
        # mp[instr[j]]= mp.get(instr[right], 0)+1
        mp[instr[right]]= right
        if len(mp.keys())==3:
            del_idx= min(mp.values())
            # mp.remove(instr[del_idx])
            left= del_idx+1
            del mp[instr[del_idx]]
        anslen= max(anslen, right-left+1)
        right+=1
    return anslen

ss='ccaabbb'
ss='eceba'
ss=''
print(longestSubstr1(ss))
