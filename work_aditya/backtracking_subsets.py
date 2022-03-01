def backtrack( nums, n, partSol, allSols):
        if n==0:
            allSols.append(partSol)
            print('all sol', allSols)
            return
        else:
            idx= n-1
            backtrack(nums, idx, partSol, allSols)
            print("partsol", partSol)
            temp_list=partSol[::]
            temp_list.append(nums[idx])
            backtrack(nums, idx, temp_list, allSols)
            print('2nd partsol', partSol)
            # partSol.pop()
            return
def soln_bk( nums):
        allSols=[]
        partialSoln=[]
        backtrack(nums, len(nums), partialSoln, allSols)
        return allSols
    
        
def subsets( nums):
        return soln_bk(nums)

nums=[1,2,3]
print(subsets(nums))