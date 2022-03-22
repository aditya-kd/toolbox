def subsetWithDup(nums, maxSum):
    nums.sort()
    allSol=[]
    partSol=[]
    backtrack(nums, 0, partSol, allSol, maxSum)
    return allSol
sumlist=[]
def backtrack(nums, idx, partSol, allSol, maxSum):
    if idx==len(nums):
        allSol.append(partSol)
        print('sum', sum(partSol))
        # maxSum=max(maxSum, sum(partSol))
        sumlist.append(sum(partSol))
        return
    k=1
    while (idx+k) < len(nums) and nums[idx]==nums[idx+k]:
        k+=1
    backtrack(nums, idx+k, partSol, allSol, maxSum)
    temp_list=partSol[::]
    temp_list.append(nums[idx])
    backtrack(nums, idx+1, temp_list, allSol, maxSum)
    

candidates = [2,-1,2,3,4,-5]
maxSum=0
subsetWithDup(candidates, maxSum)
# print(maxSum, 'is the maxsum')
print(max(sumlist))