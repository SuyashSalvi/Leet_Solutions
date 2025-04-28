from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0: 
            return False
        n = len(matrix[0])
        
        left, right = 0, m*n - 1
        while left <= right:
            mid = (left + right) // 2
            # map 1D index back into 2D
            x = mid // n
            y = mid % n
            val = matrix[x][y]
            
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False