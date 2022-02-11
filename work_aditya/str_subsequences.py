#does not take care of duplicates
def subsequences1(s,output):
    if len(s)==0:
        print(output)
        return
    subsequences1(s[1:],output+s[0])
    subsequences1(s[1:],output)

#uses backtracking
def subsequences2(str, n, curr="", index=-1):
    if index == n:
        return
    if len(curr)!=0:
        print(curr)
    
    for i in range(index+1, n):
        curr += str[i]
        subsequences2(str, n, curr, i)
        #backtrack step
        curr=curr[0:len(curr)-1]
        # print('After erase: ', curr)
    return 



output=""
subsequences1('mooomso',output)
print(output)
print('Subsequence 2')
subsequences2('moomso', len('abc'))


