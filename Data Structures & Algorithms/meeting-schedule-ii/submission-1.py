"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        sortedIntervals = sorted(intervals, key=lambda x: (x.start, x.end))
        heap = []
        numMeetingRooms = 0

        for index, interval in enumerate(sortedIntervals):
            print('start for loop', interval.start, interval.end)
            if heap: 
                minIntervalData = heapq.heappop(heap)
                minIndex = minIntervalData[1]
                minInterval = minIntervalData[2]

                if minInterval.start < interval.end and interval.start < minInterval.end:

                    print(minInterval.start, minInterval.end)
                    print(interval.start, interval.end)
                    heapq.heappush(heap, (minInterval.end, minIndex, minInterval))
                    heapq.heappush(heap, (interval.end, index, interval))
                else:
                    heapq.heappush(heap, (interval.end, index, interval))
            else:
                heapq.heappush(heap, (interval.end, index, interval))

        return len(heap)