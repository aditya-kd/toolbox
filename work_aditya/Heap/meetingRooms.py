from heapq import *

def minMeetingRooms(intervals):
        # Write your code here
        intervals.sort()
        min_heap=[]
        
        for interval in intervals:
            heappush(min_heap, (interval[1], interval[0]))
        total=0

        for interval in intervals:

# while len(min)>0 and meeting.start >= minHeap[0].end
            while(len(min_heap)!=0 and interval[1] >= min_heap[0][0]):
                heappop(min_heap)

                # heappush(min_heap, meeting)
            heappush(min_heap, (interval[1], interval[0]))
            total=max(total, len(min_heap))


        return len(min_heap)

intervals = [(0,30),(5,10),(15,20)]
print(minMeetingRooms(intervals))

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import *
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        min_heap=[]
        
        for interval in intervals:
            heappush(min_heap, (interval.end, interval.start))
        total=0

        for interval in intervals:

            while(len(min_heap)!=0 and interval.end >= min_heap[0][0]):
                heappop(min_heap)

            heappush(min_heap, (interval.end, interval.start))
            total=max(total, len(min_heap))


        return len(min_heap)



