def containsDuplicate3(arr, k):
    mp={}
    for i in range(len(arr)):
        if arr[i] in arr and abs(i-mp[arr[i]])<=k:
            return True
        else:
            mp[arr[i]]=i
        
nums = [1,2,3,1]
k=3
print (containsDuplicate3(nums, k))
