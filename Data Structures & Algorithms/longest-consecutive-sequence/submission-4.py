class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        nums.sort()
        maxCount, count = 1, 1
        print(nums)
        for i, num in enumerate(nums[1:], start=1):
            if num - 1 == nums[i-1]:
                count += 1
                maxCount = max(maxCount, count)
            elif num == nums[i-1]:
                continue
            else:
                count = 1
        
        return maxCount