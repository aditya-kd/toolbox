
def countCharWindowMinSize(text, pattern):
    mp_pat={}
    for ch in pattern:
        mp_pat[ch]= mp_pat.get(ch, 0)+1
    unique_char= len(mp_pat)
    start, end=0,0
    result={}
    anslen=0
    ans=float('inf'), None, None
    
    while end<len(text):
        
        ch = text[end]
        result[ch]= result.get(ch, 0)+1
        
        if ch in mp_pat and result[ch]==mp_pat[ch]:
            anslen+=1
        while start<= end and anslen== unique_char:
            ch= text[start]
            if end-start+1 < ans[0]:
                ans= (end-start+1, start, end)
            result[ch]-=1
            if ch in mp_pat and result[ch] < mp_pat[ch]:
                anslen-=1
                
            start+=1
        end+=1
        
    return "" if ans[0]== float("inf") else text[ans[1]:ans[2]+1]
        