class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_rec = [prices[0], 0]
        for i in range(1, len(prices)):
            min_price = min(prev_rec[0], prices[i])
            max_profit = max(prev_rec[1], prices[i] - min_price)
            prev_rec = [min_price, max_profit]

        return prev_rec[1]