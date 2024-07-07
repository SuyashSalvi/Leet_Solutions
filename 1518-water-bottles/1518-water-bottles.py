class Solution:
    def numWaterBottles(self, n: int, k: int) -> int:
        return int(n+(n-1)/(k-1))