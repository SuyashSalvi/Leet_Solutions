class Solution:
    def findMinFallingPathSum(self, matrix, row, col, dp):
        if col < 0 or col == len(matrix[0]):
            return float('inf')
        if row == len(matrix)-1:
            return matrix[row][col]
        if dp[row][col] != None:
            return dp[row][col]
        
        left = self.findMinFallingPathSum(matrix, row+1,col-1,dp)
        right = self.findMinFallingPathSum(matrix, row+1,col+1,dp)
        mid = self.findMinFallingPathSum(matrix, row+1,col,dp)

        dp[row][col] = min(left,min(right,mid)) + matrix[row][col]
        return dp[row][col]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        minSum = float('inf')
        dp = [[None] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            minSum = min(minSum, self.findMinFallingPathSum(matrix, 0, i, dp))

        return minSum