from heapq import *
def lastStoneWeight(arr ):
    max_heap=[]
    for i in arr:
        heappush(max_heap, -i)

    while len(max_heap)>1:
        y=(-heappop(max_heap))
        heapify(max_heap)
        x=(-heappop(max_heap))
        # print('After Pop',max_heap)
        # if x==y:
        #     heapify(max_heap)
        if x!=y:
            heappush(max_heap, y-x)
    # print(max_heap)
    if len(max_heap)==1:
        return max_heap[0]
    elif len(max_heap)==0:
        return 0


arr=[2,7,4,1,8,1]
print(lastStoneWeight(arr))



    
    
    



