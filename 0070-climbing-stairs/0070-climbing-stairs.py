class Solution:
    def climbStairs(self, n: int) -> int:
        # def climb(n,memo={}):
        #     if n in memo: return memo[n]
        #     if n==1: return 1
        #     if n==2: return 2
        #     memo[n] = climb(n-1,memo)+climb(n-2,memo)
        #     return memo[n]
        # return climb(n)

        def climb(i, memo = {}):
            if i in memo:
                return memo[i]

            if i > n:
                return 0

            if i == n:
                return 1

            memo[i] = climb(i + 1, memo) + climb(i + 2, memo)
            return memo[i]
        return climb(0)