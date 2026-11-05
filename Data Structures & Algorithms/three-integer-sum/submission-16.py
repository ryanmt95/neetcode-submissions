class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()

        for i in range(len(nums)-2):
            target = -nums[i]    
            left, right = i+1, len(nums)-1
            while left < right:
                if left > i+1 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                total = nums[left] + nums[right]
                if total == target:
                    if i > 0 and nums[i]==nums[i-1]:
                        left += 1
                        continue
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    
                elif total < target: 
                    left += 1
                else:
                    right -= 1
        
        return result
                

