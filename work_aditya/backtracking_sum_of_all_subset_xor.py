def subsetXORSum(nums):
    sumofAllXorToatals=0
    currentXorTotal=0
    backtrack(nums, len(nums), currentXorTotal, sumofAllXorToatals)
    return sumofAllXorToatals

def backtrack(nums, n , currentXorTotal, sumOfAllXorTotals):
    if n==0:
        sumOfAllXorTotals += currentXorTotal
        return 
    
    idx = n-1
    backtrack(nums, n-1, currentXorTotal, sumOfAllXorTotals)
    currentXorTotal = currentXorTotal ^ nums[idx]
    backtrack(nums, n-1, currentXorTotal, sumOfAllXorTotals)
    currentXorTotal = currentXorTotal ^ nums[idx]


print(subsetXORSum([1,3]))
