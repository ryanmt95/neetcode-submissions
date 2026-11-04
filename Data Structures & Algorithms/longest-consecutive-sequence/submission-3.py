class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        nums.sort()
        numMap = defaultdict(int)

        for num in nums:
            if num - 1 not in numMap:
                numMap[num] = 1
            
            else: 
                count = numMap[num-1]
                numMap[num] = count + 1
        
        return max(numMap.values())