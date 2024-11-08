class Solution:
    # def helper(self,grid,i,j):
    #     if i == len(grid) or j == len(grid[0]):
    #         return float('inf')
    #     if i == len(grid) - 1 and j == len(grid[0]) - 1:
    #         return grid[i][j]
    #     return grid[i][j] + min(self.helper(grid,i+1,j),self.helper(grid,i,j+1))
    def minPathSum(self, grid: List[List[int]]) -> int:
        # return self.helper(grid,0,0)

        # m = len(grid)
        # n = len(grid[0])
        # dp = [[0] * n for _ in range(m)]
        # for i in range(m - 1, -1, -1):
        #     for j in range(n -1, -1, -1):
        #         if i == m - 1 and j != n - 1:
        #             dp[i][j] = grid[i][j] + dp[i][j+1]
        #         elif i != m - 1 and j == n - 1:
        #             dp[i][j] = grid[i][j] + dp[i+1][j]
        #         elif i != m - 1 and j != n - 1:
        #             dp[i][j] = grid[i][j] + min(dp[i+1][j],dp[i][j+1])
        #         else:
        #             dp[i][j] = grid[i][j] 
        # return dp[0][0]

        m = len(grid)
        n = len(grid[0])
        dp = [[0] for _ in range(n)]
        for i in range(len(grid) - 1, -1, -1):
            for j in range(n -1, -1, -1):
                if i == m - 1 and j != n - 1:
                    dp[j] = grid[i][j] + dp[j+1]
                elif i != m - 1 and j == n - 1:
                    dp[j] = grid[i][j] + dp[j]
                elif i != m - 1 and j != n - 1:
                    dp[j] = grid[i][j] + min(dp[j],dp[j+1])
                else:
                    dp[j] = grid[i][j] 
        return dp[0]