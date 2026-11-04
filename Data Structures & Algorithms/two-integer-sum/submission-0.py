class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}

        for i, num in enumerate(nums):
            pair = target - num
            if pair in hashMap:
                return [hashMap[pair], i]
            
            hashMap[num] = i
        
        return []
