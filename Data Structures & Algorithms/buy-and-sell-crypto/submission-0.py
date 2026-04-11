class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for i, price in enumerate(prices):
            for j in range(i+1, len(prices)):
                temp = prices[j] - price
                if temp < 0:
                    continue
                
                if temp > profit:
                    profit = temp
        return profit