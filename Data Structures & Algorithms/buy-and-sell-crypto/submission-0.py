class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left , right = 0, 1 #left=buy, right=sell
        max_profit = 0
        while right < len(prices):
            #profit cal
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
                left = right  # we can't increase l to just 1 if r is far away and has a lower price than left.
            right += 1
        return max_profit
                
        