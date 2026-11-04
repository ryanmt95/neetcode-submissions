class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numCount = defaultdict(int)
        for n in nums: 
            numCount[n] += 1
        
        heap = []
        for num, count in numCount.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for _, num in heap]

        