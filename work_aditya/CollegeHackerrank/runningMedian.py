from heapq import *
import heapq
small=[]
large=[]
#we keep two heaps one for elements smaller than median
#and one for elements greater than median
#now the top elements in both the heaps are the 
#nearest to the median that exists, thus we can simply 
#find the median by dividing them by two and return the 
#value in float

#after running the program both the heaps will have 
#numbers greater and less than the last median, 6.0 in
#this case
def addNum(num):
    heapq.heappush(small, -1*num)

    if len(small) and len(large) and (-1*small[0])> large[0]:
        val = -1*heapq.heappop(small)
        heapq.heappush(large, val)
    
    if len(small) > len(large) +1: 
        val= -1*heapq.heappop(small)
        heapq.heappush(large, val)
    if len(large) > len(small)+1:
        val = heapq.heappop(large)
        heapq.heappush(small, -1*val)

def findMedian():
    if len(small) > len(large):
        return float(-1*small[0])
    if len(large)> len(small):
        return float(large[0])

    return ((-1*small[0])+large[0])/2

    
ls=[7,3,5,2]
ls=[12,4,5,3,8,7]
for i in ls:
    addNum(i)
    print(findMedian())