class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for i in range(len(w)):
            prefix_sum += w[i]
            self.prefix_sums.append(prefix_sum)
        self.total = prefix_sum

    def pickIndex(self) -> int:
        target = self.total * random.random()
        l, r = 0, len(self.prefix_sums)
        while l < r:
            m = l + (r - l) // 2
            if self.prefix_sums[m] < target:
                l = m + 1
            else:
                r = m

        return l
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()