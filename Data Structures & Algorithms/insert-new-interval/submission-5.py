class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        newIntervalList = []
        mergedInterval = newInterval
        isMerged = False

        for interval in intervals:
            start, end = interval[0], interval[1]
            if start <= mergedInterval[1] and mergedInterval[0] <= end:
                mergedInterval = [min(start, mergedInterval[0]), max(end, mergedInterval[1])]
            else: 
                if mergedInterval[1] < start and not isMerged:
                    newIntervalList.append(mergedInterval)
                    isMerged = True
                newIntervalList.append(interval)
        
        if not isMerged:
            newIntervalList.append(mergedInterval)

        return newIntervalList