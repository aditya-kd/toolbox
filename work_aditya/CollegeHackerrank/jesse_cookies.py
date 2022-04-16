from heapq import * 

def jesse_cookies(arr,k):
    min_heap=[]
    for i in arr:
        heappush(min_heap, i)
    
    trial=0
    while len(min_heap)>0:
        a = heappop(min_heap)
        if len(min_heap)==0 and a<k:
            return -1
        elif a>=k: break

        b= heappop(min_heap)
        operate= a+(2*b)
        trial+=1
        heappush(min_heap, operate)

    return trial

arr=[67,1,2,3,9,10]
arr=[2,7,3,6,4,6]
print(jesse_cookies(arr, 9))

