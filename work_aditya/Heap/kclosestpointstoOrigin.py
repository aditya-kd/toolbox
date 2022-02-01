from heapq import *
def kclosestPoints(points, k):
    dist=[]
    for x,y in points:
        dist.append(x*x + y*y)
    # print(dist)
    max_heap=[]
    d=k
    while d<len(max_heap):
        for i in range(k):
            heappush(max_heap, dist[i])
        data=heappop(max_heap)
        if data<dist[d+k]:
            pass
            
    # print(max_heap)
points=[[1,3],[-2,2]]
k=1

kclosestPoints(points, k)

