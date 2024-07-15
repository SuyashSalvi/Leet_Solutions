class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        r = len(pizza)
        c = len(pizza[0])
        prefix_sum = [[0 for j in range(c+1)] for j in range(r+1)]
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                cur_cell = 1 if pizza[i][j]=="A" else 0
                right_grid = prefix_sum[i+1][j]
                bottom_grid = prefix_sum[i][j+1]
                bottom_right_grid = prefix_sum[i+1][j+1]
                
                prefix_sum[i][j] = right_grid + bottom_grid - bottom_right_grid + cur_cell
        
        cache = {}
        def recurse(cur_row, cur_col, k):
            if (cur_row,cur_col,k) in cache: 
                return cache[(cur_row,cur_col,k)]  
            if prefix_sum[cur_row][cur_col] == 0: 
                return 0
            if k == 0: 
                return 1
            
            ans = 0
            for i in range(cur_row+1, r):
                if prefix_sum[cur_row][cur_col] - prefix_sum[i][cur_col] > 0:                           ans += recurse(i, cur_col, k-1)
            for j in range(cur_col+1,c):
                if prefix_sum[cur_row][cur_col] - prefix_sum[cur_row][j] > 0:
                    ans += recurse(cur_row, j, k-1)
            cache[(cur_row,cur_col,k)] = ans         
            return ans
        return recurse(0,0,k-1) % (10**9+7)