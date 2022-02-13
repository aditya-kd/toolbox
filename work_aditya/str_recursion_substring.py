from copy import copy as cp
global result
def subsets( nums):
        result = []
        solve(0, nums, [])
        return result
        
def solve( i, nums, out):
        
        if i==len(nums):
            result.append(out)
            return
        
        out1 =  cp.deepcopy(out)
        out2 = cp.deepcopy(out)
        
        out1.append(nums[i])
        solve(i+1, nums, out1)
        solve(i+1, nums, out2)

instr=[1,2,3]
subsets(instr)
