from collections import deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # The nodes are labeled from 1 to n.
        # We'll convert them to 0-indexed.
        graph = [[] for _ in range(n)]
        for u, v in edges:
            # Convert to 0-indexed
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        
        # color array for bipartite check: -1 means uncolored; 0 and 1 are two colors.
        color = [-1] * n
        components = []  # Each component will be a list of nodes (0-indexed)
        
        # DFS function that colors a component and checks bipartiteness.
        def dfs(u: int, c: int, comp: List[int]) -> bool:
            color[u] = c
            comp.append(u)
            for v in graph[u]:
                if color[v] == -1:
                    if not dfs(v, 1 - c, comp):
                        return False
                elif color[v] == c:
                    # Conflict: same color on both ends of an edge.
                    return False
            return True
        
        # Find all connected components; also check bipartiteness.
        for i in range(n):
            if color[i] == -1:
                comp = []
                if not dfs(i, 0, comp):
                    return -1  # Not bipartite → impossible to group nodes as required.
                components.append(comp)
        
        # For each connected component, compute the maximum distance (in terms of BFS levels)
        # from any node in the component. The maximum number of groups for this component
        # is the maximum distance plus 1.
        def bfs(start: int) -> int:
            # Standard BFS that computes the distance from start to all other nodes in the component.
            dist = {start: 0}
            q = deque([start])
            max_d = 0
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v not in dist:
                        dist[v] = dist[u] + 1
                        max_d = max(max_d, dist[v])
                        q.append(v)
            return max_d
        
        total_groups = 0
        for comp in components:
            comp_max = 0
            # For each node in the component, run BFS to see the maximum distance (depth) in that component.
            for u in comp:
                comp_max = max(comp_max, bfs(u))
            # The number of groups for this component is the maximum BFS depth + 1.
            total_groups += (comp_max + 1)
        
        return total_groups