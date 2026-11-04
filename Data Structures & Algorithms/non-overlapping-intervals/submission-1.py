class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        numRemoved = 0
        sortedIntervals = sorted(intervals)
        previous = sortedIntervals[0]

        for interval in sortedIntervals[1:]:
            if interval[0] < previous[1] and previous[0] < interval[1]:
                numRemoved += 1
                if previous[1] > interval[1]:
                    previous = interval
            else:
                previous = interval
        
        return numRemoved