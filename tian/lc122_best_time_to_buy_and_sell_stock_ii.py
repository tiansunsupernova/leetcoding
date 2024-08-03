from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = prices[0]
        total = 0
        for i in range(1, len(prices)):
            if prices[i] > x:
                total += prices[i] - x
            x = prices[i]
        return total