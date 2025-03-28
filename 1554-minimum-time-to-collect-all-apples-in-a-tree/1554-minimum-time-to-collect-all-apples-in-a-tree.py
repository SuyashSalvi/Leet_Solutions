class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        def dfs(node, parent):
            totalTime = 0
            for child in adj[node]:
                if child == parent:
                    continue
                childTime = dfs(child, node)
                if childTime > 0 or hasApple[child]:
                    totalTime += childTime + 2

            return totalTime

        return dfs(0, -1)