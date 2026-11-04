class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numMap = dict()

        for index, num in enumerate(nums):
            num2 = target - num

            if num2 in numMap:
                return [numMap[num2], index]
            
            numMap[num] = index
        
        return []
        