from heapq import *
def kthsmallest(arr, k):
    min_heap=[]
    for i in arr:
        heappush(min_heap, i)
    for i in range(0,k-1):
        heappop(min_heap)
        print('pass',min_heap)
    
    print(min_heap[0])
    
    
k=int(input())
arr=map(int, input().split())
kthsmallest(arr, k)
