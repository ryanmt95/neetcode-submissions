class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0: 
            return 0
        
        numSet = set(nums)
        maxCount = 1

        for num in numSet:
            if num - 1 not in numSet:
                count = 1

                while num + 1 in numSet:
                    num += 1
                    count += 1
                
                maxCount = max(maxCount, count)
        
        return maxCount
