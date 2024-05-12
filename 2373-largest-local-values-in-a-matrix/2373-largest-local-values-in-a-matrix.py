class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        r = len(grid)
        c = len(grid[0])
        
        res = [[0] * (c-2) for _ in range(r-2)]
        
        for i in range(1,r-1):
            for j in range(1,c-1):
                for di in [-1,0,1]:
                    for dj in [-1,0,1]:
                        res[i-1][j-1] = max(res[i-1][j-1], grid[i+di][j+dj])
        return res