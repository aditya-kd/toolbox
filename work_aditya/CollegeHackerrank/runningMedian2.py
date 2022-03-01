from queue import PriorityQueue
 
INT_MAX = 10000000000
 
def findMedian(arr, n):
    lowerHalf = PriorityQueue()
    higherHalf = PriorityQueue()
    for size in range(1, n + 1):
 
        x = INT_MAX
        if lowerHalf.qsize() > 0:
 
            x = abs(lowerHalf.get())
            lowerHalf.put(-x)
 
        if lowerHalf.qsize() > 0 and x > arr[size - 1]:
            lowerHalf.put(-(arr[size - 1]))
 
            if lowerHalf.qsize() > higherHalf.qsize() + 1:
                higherHalf.put(abs(lowerHalf.get()))
 
        else:
 
            higherHalf.put(arr[size - 1])
 
            if higherHalf.qsize() > lowerHalf.qsize() + 1:
                lowerHalf.put(-(higherHalf.get()))
 
        if size % 2 == 1:
 
            if higherHalf.qsize() > lowerHalf.qsize():
 
                median = higherHalf.get()
                higherHalf.put(median)
 
            else:
 
                median = abs(lowerHalf.get())
                lowerHalf.put(-median)
 
        else:
 
            a = lowerHalf.get()
            lowerHalf.put(a)
            b = higherHalf.get()
            higherHalf.put(b)
 
            median = (abs(a) + b) // 2
 
        print(median, end=" ")