class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countMap = defaultdict(int)

        for num in nums:
            countMap[num] += 1
        
        heap = []

        for num, count in countMap.items():
            heapq.heappush(heap, (-count, num))
        
        most_frequent_nums = []

        for _i in range(k):
            if len(heap) == 0:
                break
            num = heapq.heappop(heap)[1]
            most_frequent_nums.append(num)
        
        return most_frequent_nums