class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        prev, cur = 0, 1
        for i in range(n-1):
            prev, cur = cur, prev + cur
        return cur