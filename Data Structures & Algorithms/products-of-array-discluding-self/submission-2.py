class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]
        suffix = [1]

        for n in nums:
            prefix.append(prefix[-1] * n)
        
        for n in nums[::-1]:
            suffix.append(suffix[-1]*n)
        suffix = suffix[::-1]

        return [prefix[i] * suffix[i+1] for i in range(len(nums))]
        # total = 1
        # zeroCount = 0
        # for num in nums:
        #     if num != 0:
        #         total *= num
        #     else:
        #         zeroCount += 1

        # if zeroCount > 1:
        #     return [0 for _ in range(len(nums))]

        # if zeroCount == 0:
        #     return [int(total/num) for num in nums]

        # else:
        #     return [total if num == 0 else 0 for num in nums]        
