class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mostProfit = 0
        lowestPrice = float('inf')

        for price in prices:
            lowestPrice = min(lowestPrice, price)
            mostProfit = max(mostProfit, price - lowestPrice)
        
        return mostProfit