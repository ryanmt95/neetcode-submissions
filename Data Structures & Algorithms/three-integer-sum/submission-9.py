class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -num

            left, right = i + 1, len(nums) - 1
            while left < right: 
                total = nums[left] + nums[right]
                if total == target: 
                    res.append([num, nums[left], nums[right]])

                    left += 1

                    while left < len(nums) and nums[left] == nums[left-1]:
                        left += 1
                elif total < target:
                    left += 1
                elif total > target:
                    right -= 1
        
        return res