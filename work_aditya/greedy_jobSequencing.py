import heapq
def jobsequencing(jobs):
    n= len(jobs)
    jobs.sort(key=lambda x:x[1])
    result=[]
    maxheap=[]
    for i in range(n-1, -1, -1):
        if i==0:
            slot= jobs[i][1] #deadling at index 1
        else:
            slot= jobs[i][1] - jobs[i-1][1]
        
        heapq.heappush(maxheap, (-jobs[i][2], jobs[i][1], jobs[i][0]))
        while slot and maxheap:
            p,d,id= heapq.heappop(maxheap)
            slot-=1
            result.append([id, d])
    result.sort(key= lambda x:x[1])#according to deadline
    print(result)
    return result

arr=[['a', 2, 100],['b',1,19], ['c',2 ,27],['d',1,25],['e', 3, 15]]
jobsequencing(arr)
