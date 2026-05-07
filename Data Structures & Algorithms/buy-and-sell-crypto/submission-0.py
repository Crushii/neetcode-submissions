class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            j = i+1

            while j < len(prices):
                max_profit = max((prices[j] - prices[i]), max_profit)
                j+=1

        return max_profit
        