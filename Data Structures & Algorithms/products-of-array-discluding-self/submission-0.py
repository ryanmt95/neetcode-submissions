class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total = 1
        zeroCount = 0
        for num in nums:
            if num != 0:
                total *= num
            else:
                zeroCount += 1

        if zeroCount > 1:
            return [0 for _ in range(len(nums))]

        if zeroCount == 0:
            return [int(total/num) for num in nums]

        else:
            return [total if num == 0 else 0 for num in nums]        
