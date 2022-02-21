import math


def mcm(values, i, j):
    if i==j: 
        return 0
    min_val= math.inf
    for k in range(i, j):
        temp_val= mcm(values,i,k)+mcm(values, k+1, j)+values[i-1]*values[k]*values[j]
        if temp_val < min_val:
            min_val = temp_val
        
    return min_val

def minScoreTriangulate(values):
    ans = mcm(values, 1, len(values)-1)
    return ans

if __name__ =='__main__':
    values = [1,3,1,4,1]