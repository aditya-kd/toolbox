import math

def isPalindromic(string, i, j):
    return (string[i:j+1]) == string[i: j+1][::-1]

def mcm(string, i, j):
    if i==j or isPalindromic(string , i, j):
        return 0
    
    min_val=math.inf
    
    for k in range(i, j):
        temp_val = 1+mcm(string, i, k) + mcm(string, k+1, j)
        if temp_val < min_val:
            min_val= temp_val
    return min_val
def palindromicPartitioning(string):
    ans = mcm(string, 0, len(string)-1)
    return ans

#apprach 2
def isPal(s, l,r):
    while l<r:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True

def parition(s):
    res=[]
    part=[]
    def dfs(i):
        if i>= len(s):
            res.append(part[::])
            return 
        for j in range(i, len(s)):
            if isPal(s, i,j):
                part.append(s[i:j+1])
                dfs(j+1)
                part.pop()
    dfs(0)
    return res
if __name__ == '__main__':
    string ='aab'
    # ans = palindromicPartitioning(string)
    # print(ans)
    print(parition(string))

