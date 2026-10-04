
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        min_price=prices[0]
        max_profit_seen=prices[1]-prices[0]
        for i in prices :
            if i<=min_price:
                min_price=i
            if i-min_price>=max_profit_seen:
                max_profit_seen=i-min_price
            print(max_profit_seen)
        return max_profit_seen

            
                