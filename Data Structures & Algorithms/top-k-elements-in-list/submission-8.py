class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = [[] for _ in range(len(nums)+1)]
        numCount = defaultdict(int)
        for n in nums:
            numCount[n] += 1

        for num, count in numCount.items():
            freqMap[count].append(num)

        topK = []
        for num in range(len(nums), -1, -1):
            numList = freqMap[num]
            for num in numList:
                topK.append(num)

                if len(topK) == k:
                    return topK
        
        return []

        # # heap solution
        # numCount = defaultdict(int)
        # for n in nums: 
        #     numCount[n] += 1
        
        # heap = []
        # for num, count in numCount.items():
        #     heapq.heappush(heap, (count, num))

        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # return [num for _, num in heap]

        