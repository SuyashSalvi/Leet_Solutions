from typing import List
from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        """
        Return the minimum number of transactions required to settle all debts.
        """

        # 1) Compute net balance for each person
        net_balance = defaultdict(int)
        for payer, payee, amount in transactions:
            net_balance[payer] -= amount
            net_balance[payee] += amount

        # 2) Filter out zero balances (already settled)
        debts = [bal for bal in net_balance.values() if bal != 0]

        def dfs(start: int) -> int:
            """
            Try to settle debts[start:] with minimal transactions.
            Returns the minimal number of additional transactions needed.
            """
            # Skip already‐settled positions
            while start < len(debts) and debts[start] == 0:
                start += 1

            # If everyone is settled, no more transactions needed
            if start == len(debts):
                return 0

            min_tx = float('inf')
            seen = set()  # Prune identical attempts

            # Attempt to settle debts[start] with any opposite‐signed debt
            for i in range(start + 1, len(debts)):
                if debts[i] * debts[start] < 0 and debts[i] not in seen:
                    seen.add(debts[i])
                    # Simulate one transaction between start and i
                    debts[i] += debts[start]
                    # Count this transaction + recursion on the rest
                    min_tx = min(min_tx, 1 + dfs(start + 1))
                    # Backtrack
                    debts[i] -= debts[start]
                    # If it perfectly cancels debts[start], no need to try others
                    if debts[i] + debts[start] == 0:
                        break

            return min_tx

        return dfs(0)