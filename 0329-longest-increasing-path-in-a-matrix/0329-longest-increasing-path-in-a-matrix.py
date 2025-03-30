from collections import deque
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        indegree = [[0] * n for _ in range(m)] 
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(m):
            for j in range(n):
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        indegree[x][y] += 1
        q = deque()
        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    q.append((i, j))
        level = 0
        while q:
            level += 1
            q_len = len(q)
            for _ in range(q_len):
                i, j = q.popleft()
                for dx, dy in directions:
                    x, y = i + dx, j+ dy
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        indegree[x][y] -= 1
                        if indegree[x][y] == 0:
                            q.append((x, y))
        return level
        
        
        
        
        
        
        
        # if not matrix or not matrix[0]:
        #     return 0

        # m, n = len(matrix), len(matrix[0])
        # # Directions for movement: right, down, left, up.
        # directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        # # Initialize the indegree matrix with zeros.
        # indegree = [[0] * n for _ in range(m)]
        
        # # For every cell, look at its neighbors.
        # # If neighbor's value is greater, then there is an edge from current cell to neighbor.
        # # We increment the indegree of the neighbor.
        # for i in range(m):
        #     for j in range(n):
        #         for dx, dy in directions:
        #             x, y = i + dx, j + dy
        #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
        #                 indegree[x][y] += 1
        
        # # Initialize a deque with all cells having indegree 0 (i.e. no incoming edge).
        # q = deque()
        # for i in range(m):
        #     for j in range(n):
        #         if indegree[i][j] == 0:
        #             q.append((i, j))
        
        # # 'level' will count the number of layers (or steps) we process.
        # level = 0
        
        # # Process the graph level by level.
        # # At each level, we "remove" nodes with indegree 0 (i.e. peel off one layer).
        # while q:
        #     level += 1
        #     # Process all nodes at the current layer.
        #     for _ in range(len(q)):
        #         i, j = q.popleft()
        #         for dx, dy in directions:
        #             x, y = i + dx, j + dy
        #             # Only consider valid moves that form an increasing path.
        #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
        #                 indegree[x][y] -= 1
        #                 # If after decrementing, the neighbor becomes "ready" (indegree 0),
        #                 # add it to the queue for the next layer.
        #                 if indegree[x][y] == 0:
        #                     q.append((x, y))
        
        # # The number of levels processed equals the length of the longest increasing path.
        # return level