class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        minRate, maxRate = 1, max(piles)
        res = maxRate

        while minRate <= maxRate:
            rate = (minRate + maxRate) // 2

            timeTaken = 0
            for pile in piles:
                timeTaken += math.ceil(pile/rate)

            if timeTaken <= h:
                res = rate
                maxRate = rate - 1
            else:
                minRate = rate + 1
        
        return res