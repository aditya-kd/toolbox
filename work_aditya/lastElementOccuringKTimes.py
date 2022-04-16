
import heapq
def topKFrequent(nums, k):
    maxheap=[]
    mp={}
    for item in nums:
        mp[item]=mp.get(item,0)+1
    # print(mp)
    for item, fr in mp.items():
        heapq.heappush(maxheap, (-fr, item))
    # print(maxheap)
    res=[]
    while k>0:
        pair= heapq.heappop(maxheap)
        
def func2(arr, k):
    mp={}
    for ch in arr:
        mp[ch]= mp.get(ch, 0)+1
    print(mp)
    res=[]
    for x in mp.keys():
        if mp[x]==k:
            res.append(x)
    print(res)
    return res[-1]

        
arr=[1,1,1,2,2,3]
arr=[2,3,4,2,3,7,3,3,8,2]
arr=[2,3,4,2,3,4,2,3,4]

k=3
print(func2(arr, k))

# nums = [1,1,1,2,2,3], k = 2
