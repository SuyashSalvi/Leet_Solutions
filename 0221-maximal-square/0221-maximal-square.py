class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0]) if row else 0
        dp = [0] * (col + 1)
        maxsqlen = 0
        prev = 0

        for i in range(1,row+1):
            for j in range(1,col+1):
                temp = dp[j]
                if matrix[i-1][j-1] == "1":
                    dp[j] = min(dp[j],min(prev, dp[j-1])) + 1
                    maxsqlen = max(maxsqlen, dp[j])
                else:
                    dp[j] = 0

                prev = temp

        return maxsqlen ** 2