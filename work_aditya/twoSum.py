def twoSum( nums, target):
        mp={}
        
        for i in range(0, len(nums)):
            
            dif=target+nums[i]
            if dif in mp:
                print( [mp[dif], i])
            else:
                mp[nums[i]]=i
        return
    


ls=[1,5,3,4,2]
target=2
print(twoSum(ls, target))