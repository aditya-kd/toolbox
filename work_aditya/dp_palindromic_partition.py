import math

def isPalindromic(string, i, j):
    return (string[i:j+1])== string[i: j+1][::-1]

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

if __name__ == '__main__':
    string ='abcd'
    ans = palindromicPartitioning(string)
    print(ans)
