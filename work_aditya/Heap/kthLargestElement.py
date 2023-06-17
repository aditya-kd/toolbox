from heapq import *
def kthLargest(arr, k):
    min_heap=[]
    for i in arr:
        heappush(min_heap, i)
    #heap creatd

#we traverse from k length to end
    for i in range(k, len(arr)):
        heappop(min_heap)
        heappush(min_heap, arr[i])

    return min_heap[0]

arr=[3,4,2,3,6,76,8,9]
k=3
print('From Function')
print(kthLargest(arr, k))
# print('From Sorting')
# arr.sort()
print(arr)



