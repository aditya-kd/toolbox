def countAnagrams(text, pattern):
    mp={}
    for ch in pattern:
        mp[ch]= mp.get(ch, 0)+1
    # print(mp)
    letters=mp.keys()
    # print(letters)
    count=len(letters)
    size=len(text)
    k=len(pattern)
    ans=0
    i=0
    j=0
    while j<size:
        if text[j] in letters:
            mp[text[j]]-=1
            if mp[text[j]] == 0:
                count-=1
            
        if j-i+1 < k:
            j+=1
        elif j-i+1 == k:
            if count==0:
                ans+=1
                print('index', i,j)
#we slide the window so we restore the frequency in the map in line 28
            if text[i] in letters:
                    mp[text[i]]+=1
                    if mp[text[i]]==1:
                        count+=1
            i+=1
            j+=1
    return ans


            
        


arr='forxxorfxdofr'
p='for'
arr='abhcdfvgcabthilbac'
p='abc'
arr='axbxcxdxfxbcaxvcbxabc'
p='abc'

print(countAnagrams(arr, p))
        
