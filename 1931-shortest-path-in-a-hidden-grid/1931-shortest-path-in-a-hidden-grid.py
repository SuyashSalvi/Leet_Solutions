# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> None:
#        
#
#    def isTarget(self) -> bool:
#        
#

import collections

class Solution:
    def findShortestPath(self, master: 'GridMaster') -> int:
        # Directions for moving in the grid.
        dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        # Opposite directions for backtracking.
        opp = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
        
        # Map to record the discovered grid:
        # grid[(x, y)] = True if cell is reachable (empty or target), False if blocked.
        grid = {}
        start = (0, 0)
        grid[start] = True
        target = None  # Will store the coordinate of the target if found.
        
        # Phase 1: DFS exploration to build the grid.
        def dfs(x: int, y: int):
            nonlocal target
            if master.isTarget():
                target = (x, y)
            # Try all four directions.
            for d in dirs:
                dx, dy = dirs[d]
                nx, ny = x + dx, y + dy
                # Only explore if we haven't visited this cell.
                if (nx, ny) not in grid and master.canMove(d):
                    master.move(d)
                    grid[(nx, ny)] = True
                    dfs(nx, ny)
                    # Backtrack to previous cell.
                    master.move(opp[d])
                # If we haven't seen the cell and can't move, mark it as blocked.
                elif (nx, ny) not in grid:
                    grid[(nx, ny)] = False
        
        dfs(0, 0)
        
        # If target was never reached during exploration, return -1.
        if target is None:
            return -1
        
        # Phase 2: BFS to find the shortest path from start to target.
        queue = collections.deque([(0, 0, 0)])  # (x, y, distance)
        seen = {(0, 0)}
        while queue:
            x, y, dist = queue.popleft()
            if (x, y) == target:
                return dist
            for dx, dy in dirs.values():
                nx, ny = x + dx, y + dy
                if (nx, ny) in grid and grid[(nx, ny)] and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
        
        return -1
