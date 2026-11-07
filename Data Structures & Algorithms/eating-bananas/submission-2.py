class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 0, max(piles)

        while left <= right:
            rate = (left+right)//2
            timeTaken = self.eatRateTimeTaken(piles, rate) if rate > 0 else float('inf')
            timeTaken2 = self.eatRateTimeTaken(piles, rate-1) if rate > 1 else float('inf')

            if timeTaken <= h and timeTaken2 > h:
                return rate
            
            if timeTaken > h:
                left = rate + 1
            else:
                right = rate - 1
        
        return -1
    
    # time complexity: O(n) 
    def eatRateTimeTaken(self, piles, rate):
        timeTaken = 0
        for pile in piles:
            timeTaken += math.ceil(pile/rate)
        
        return int(timeTaken)