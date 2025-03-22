class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1

        def get_neighbours(row, col):
            for dr,dc in directions:
                new_row = row + dr
                new_col = col + dc
                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)

        if grid[0][0] == 1 or grid[max_row][max_col] == 1:
            return -1

        q = deque()
        q.append((0,0))
        grid[0][0] = 1
        
        while q:
            
            row, col = q.popleft()
            distance = grid[row][col]

            if [row, col] == [max_row, max_col]:
                return distance

            for new_row, new_col in get_neighbours(row, col):
                grid[new_row][new_col] = distance + 1
                q.append((new_row, new_col))
        return -1