class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_seen=float('inf') # Set to infinity initially
        max_profit=0
        for price in prices:
            if price<min_price_seen:
                min_price_seen=price
            elif price - min_price_seen > max_profit:
                max_profit = price - min_price_seen         
        return max_profit