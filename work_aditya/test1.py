def genSubstring(nums, n, partSol,allSol):
    if n==0:
        allSol.append(''.join(partSol))
        return 
    else:
        idx=n-1
        #without
        genSubstring(nums, idx, partSol, allSol)
        temp=partSol[::]
        temp.append(nums[idx])
        genSubstring(nums, idx, temp, allSol)
def solve(nums):
    allSol=[]
    partSol=[]
    genSubstring(nums, len(nums), partSol, allSol)
    return allSol

s='abc'
print(solve(s))

