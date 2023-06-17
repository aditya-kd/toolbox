import sys
def minSubArrayLen(self, target: int, nums):
        n= len(nums)
        ans = sys.maxsize
        start=0
        ssum=0
        i=0
        while i < n:
            ssum+= nums[i]
            while ssum >=target:
                if i-start+1 < ans:
                    ans=i-start+1
                ssum-= nums[start]
                start+=1
            i+=1
        if ans==sys.maxsize:
            return 0
        return ans