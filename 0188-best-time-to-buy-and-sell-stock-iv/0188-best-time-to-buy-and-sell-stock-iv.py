from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        Max profit with at most k transactions.
        If k >= n//2, it's unlimited transactions: sum all positive diffs.
        Otherwise use O(n·k) DP with O(k) space.
        """
        n = len(prices)
        if n < 2 or k == 0:
            return 0

        # Unlimited transactions case
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                profit += max(0, prices[i] - prices[i-1])
            return profit

        # buy[t]: max profit after t buys (holding stock)
        # sell[t]: max profit after t sells (no stock)
        buy  = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for t in range(1, k + 1):
                # either keep previous buy[t], or buy now using sell[t-1] cash
                buy[t]  = max(buy[t],  sell[t-1] - price)
                # either keep previous sell[t], or sell now what we bought at buy[t]
                sell[t] = max(sell[t], buy[t] + price)

        return sell[k]