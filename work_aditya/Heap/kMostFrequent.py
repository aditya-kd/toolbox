import heapq

def topKFrequent(nums, k):
    maxheap=[]
    mp={}
    for item in nums:
        mp[item]=mp.get(item,0)+1
    print(mp)
    for item, fr in mp.items():
        heapq.heappush(maxheap, (-fr, item))
    print(maxheap)
    while k>0:
        pair= heapq.heappop(maxheap)
        print(pair[1])
        k-=1



ls=[1,1,1,2,2,3]
topKFrequent(ls,2)
    
        