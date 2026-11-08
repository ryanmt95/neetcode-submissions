class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1

        while left <= right: 
            mid = (left + right) // 2
            num = nums[mid]

            if num == target:
                return mid
            
            if nums[0] <= num:
                if nums[0] <= target < num:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if num < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1