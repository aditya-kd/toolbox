def backtrack(self, nums, n, partSol, allSols):
        if n==0:
            allSols.append(partSol)
            return
        else:
            idx= n-1
            self.backtrack(nums, n-1, partSol, allSols)
            temp_list=partSol[::]
            temp_list.append(nums[idx])
            self.backtrack(nums, n-1, temp_list, allSols)
            # partSol.pop()
            return
    def soln_bk(self, nums):
        allSols=[]
        partialSoln=[]
        self.backtrack(nums, len(nums), partialSoln, allSols)
        return allSols
    
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.soln_bk(nums)