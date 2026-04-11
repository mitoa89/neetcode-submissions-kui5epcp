class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        buy_day = 0
        sell_day = buy_day + 1
        while sell_day < len(prices):
            profit = prices[sell_day] - prices[buy_day]

            if profit > 0:
                max_profit = max(profit, max_profit)
            else:
                buy_day = sell_day

            sell_day +=1

       # for i, price in enumerate(prices):
      #      for j in range(i+1, len(prices)):
      #          temp = prices[j] - price
        #        if temp < 0:
       #             continue
                
        #        if temp > profit:
        #            profit = temp
        return max_profit