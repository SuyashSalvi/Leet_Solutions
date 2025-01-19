class Solution:
    def __init__(self):
        self.mark = {}
        self.dp = {}

    def jumps(self, stones, n, i, prevJump):
            if i == n - 1:
                return True

            if (i,prevJump) in self.dp:
                return self.dp[(i,prevJump)]

            ans = False

            for nextJump in [prevJump - 1, prevJump, prevJump + 1]:
                if nextJump > 0 and stones[i] + nextJump in self.mark:
                    ans = ans or self.jumps(stones, n, self.mark[stones[i] + nextJump], nextJump)
            self.dp[(i,prevJump)] = ans
            return ans

    def canCross(self, stones: List[int]) -> bool:
        for i, s in enumerate(stones):
            self.mark[s] = i
            
        return self.jumps(stones, len(stones), 0, 0)