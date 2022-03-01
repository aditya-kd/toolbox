def subsetWithDup(nums):
    nums.sort()
    allSol=[]
    partSol=[]
    backtrack(nums, 0, partSol, allSol)
    return allSol
def backtrack(nums, idx, partSol, allSol):
    if idx==len(nums):
        allSol.append(partSol)
        return
    k=1
    while (idx+k) < len(nums) and nums[idx]==nums[idx+k]:
        k+=1
    backtrack(nums, idx+k, partSol, allSol)
    temp_list=partSol[::]
    temp_list.append(nums[idx])
    backtrack(nums, idx+1, temp_list, allSol)
    

candidates = [1,2,2]

print(subsetWithDup(candidates))

