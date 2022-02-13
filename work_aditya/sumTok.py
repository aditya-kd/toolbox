#using two nested loops
def findSumtoK(arr, k):
    n=len(arr)
    for i in range(0, n):
        for j in range(1, n):
            if arr[i]+arr[j] == k:
                print(arr[i],arr[j])
                
#using hashing 
def twoSum(nums, target):
        mp={}
        for i in range(0, len(nums)):
            
            dif=target-nums[i]
            if dif in mp:
                print(dif, nums[i])
            else:
                mp[nums[i]]=i
        return
def findPairs(arr, k):
    mp={}
    total=0
    for i in range(0, len(arr)):
        dif=k+arr[i]
        if dif in mp:
            total+=1
        else:
            mp[arr[i]]=i
    return total


#using two pointer from both ends
def twoSum2(arr, k):
    arr.sort()
    start=0
    end=len(arr)-1
    total=0
    while(start<end):
        sum=arr[start]+arr[end]
        if arr[start]+k==arr[end]:
            print(arr[start], arr[end])
            total+=1
            break
        elif sum>k:
            end-=1
        else:
            start+=1
    return total


arr=[ 1, 2, 5, 6, 9, 10]
k=2
# print(findSumtoK(arr, k))
# print(twoSum(arr, k))

# print(twoSum2(arr, k))
arr=[ 1, 2, 3, 4, 5, 6 ]
k=2
print(findPairs(arr, k))

