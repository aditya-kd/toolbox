from collections import deque


class Solution:
    def maxSlidingWindow(self, nums,k):#gives tle , i don't know why
        ans=[]
        i,j=0,0
        
        while j< len(nums):
            
            if j-i+1<k:
                j+=1
                
            elif j-i+1==k:
                
                ans.append(max(nums[i:j+1]))
                i+=1
                j+=1
                

        print(ans)
    
    def maxSlidingWindow2(self,nums,k):
        queue=deque()
        res=[]
        for i , curval in enumerate(nums):
            while queue and nums[queue[-1]] <= curval:
                queue.pop()

            queue.append(i)

            if queue[0] == i-k:
                queue.popleft()

            if i>= k-i:
                res.append(nums[queue[0]])

        print(res)
        return res



s=Solution()

ls=[1,3,-1,-3,5,3,6,7]
k=3
ls=[1]
k=1
s.maxSlidingWindow2(ls,k)

            
            
        