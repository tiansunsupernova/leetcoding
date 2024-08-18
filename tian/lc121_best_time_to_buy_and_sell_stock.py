from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_price = float("inf")
        max_profit = 0
        for price in prices:
            profit = price - low_price
            if profit > max_profit:
                max_profit = profit        
            if price < low_price:
                low_price = price
        return max_profit