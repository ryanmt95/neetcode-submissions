class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        maxLength = 0
        for n in nums:
            if n - 1 not in numSet:
                current = n
                while current in numSet:
                    current += 1
                
                length = current - n
                maxLength = max(maxLength, length)
        
        return maxLength