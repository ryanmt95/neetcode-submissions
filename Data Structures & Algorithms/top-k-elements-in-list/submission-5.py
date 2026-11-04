class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = defaultdict(int)
        frequency_array = [[] for _ in range(len(nums))]

        for num in nums:
            counts[num] += 1
        
        for num, count in counts.items():
            frequency_array[count-1].append(num)

        top_k_freq = []
        for numList in frequency_array[::-1]:
            for num in numList:
                top_k_freq.append(num)
                if len(top_k_freq) == k:
                    return top_k_freq
            
        return top_k_freq