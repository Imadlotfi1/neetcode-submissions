
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices=prices[0]
        max_profit=0
        for i in range (len(prices)):
            if prices[i]<= min_prices:
                min_prices=prices[i]
            l=prices[i]-min_prices
            if l>max_profit:
                max_profit=l
        return max_profit
            
                