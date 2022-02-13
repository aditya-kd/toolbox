#does not take care of duplicates
res1=[]
def subsequences1(s,output):
    if len(s)==0:
        # print(output)
        res1.append(output)
        return
    subsequences1(s[1:],output+s[0])
    subsequences1(s[1:],output)

#uses backtracking
res2=[]
def subsequences2(str, n, curr="", index=-1):
    if index == n:
        return
    if len(curr)!=0:
        # print(curr)
        res2.append(curr)
    
    for i in range(index+1, n):
        curr += str[i]
        subsequences2(str, n, curr, i)
        #backtrack step
        curr=curr[0:len(curr)-1]
        # print('After erase: ', curr)
    return 

output=""
instr='moomso'
slen=len(instr)

subsequences1(instr,output)
subsequences2(instr, slen)

print('Second function')
res1.sort()
res2.sort()

print(res1, len(res1))
print(res2, len(res2))
print(res1 == res2)