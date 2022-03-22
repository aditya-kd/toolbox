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

def separate(i, s, partSol, res):#this is s type of dfs
    if i>=len(s):
        res.append(partSol[::])
        return
    for j in range(i, len(s)):
        if isPal(s, i,j):
            temp=partSol[::]
            temp.append(s[i:j+1])
            # partSol.append(s[i:j+1])
            separate(j+1, s, temp, res)
            partSol.pop()
    return res
def rahulsir(s, dp):
    n=len(s)
    res=[]
    for j in range(1, len(s)):
        for i in range(j, 0, -1):
            if dp[i][j]:
                mini = min(mini, res[i-1])
                res[i]= mini+1
    print(res[n-1])
def parition(s):
    res=[]
    part=[]
    # def separateinside(i):
    #     if i>= len(s):
    #         res.append(part[::])
    #         return 
    #     for j in range(i, len(s)):
    #         if isPal(s, i,j):
    #             part.append(s[i:j+1])
    #             separateinside(j+1)
    #             part.pop()


    separate(0)
    return res
if __name__ == '__main__':
    string ='eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj'
    ans = palindromicPartitioning(string)
    print(ans)
    # finalans=parition(string)
    # print('No of cuts')
    # print(len(finalans[-1])-1)
    # for i in (parition(string)):
    #     print(i)


