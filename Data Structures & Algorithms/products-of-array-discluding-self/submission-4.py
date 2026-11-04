class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = 1
        suffix = 1

        res = [1 for _ in range(len(nums))]

        for i, n in enumerate(nums):
            res[i] = prefix
            prefix *= n
        
        for j in range(len(nums)-1, -1, -1):
            res[j] = res[j] * suffix
            num = nums[j]
            suffix *= num
        
        return res
