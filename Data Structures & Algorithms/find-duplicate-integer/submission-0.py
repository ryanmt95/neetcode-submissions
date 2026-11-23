class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        numMap = dict()

        for num in nums:
            if num in numMap:
                return num
            
            numMap[num] = True
        
        return False
        