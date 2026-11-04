class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        sortedIntervals = sorted(intervals)
        previousInterval = sortedIntervals[0]
        mergedIntervals = []

        for interval in sortedIntervals[1:]:
            start, end = interval[0], interval[1]
            prevStart, prevEnd = previousInterval[0], previousInterval[1]

            if start <= prevEnd and prevStart <= end:
                previousInterval = [min(start, prevStart), max(end, prevEnd)]
            else:
                mergedIntervals.append(previousInterval)
                previousInterval = interval

        mergedIntervals.append(previousInterval)

        return mergedIntervals