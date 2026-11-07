class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if nums[0] <= nums[-1]:
            return nums[0]
        
        left, right = 1, len(nums)

        while left <= right: 
            index = (left+right)//2

            if nums[index-1] > nums[index]:
                return nums[index]
            
            if nums[0] > nums[index]:
                right = index - 1
            else:
                left = index + 1
        
        return -1