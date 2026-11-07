class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1

        while left <= right: 
            index = (left+right)//2
            num = nums[index]

            if num == target:
                return index
            
            if target > num:
                left = index + 1
            
            else:
                right = index - 1
    
        return -1