class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # base case
        if n < 2: return 1

        # graph
        graph = defaultdict(set)
        res = 0
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)

        # bfs - from leaf nodes
        q = deque(node for node, neigh in graph.items() if len(neigh) == 1)
        while q:
            node = q.popleft()
            nnode = (next(iter(graph[node])) if graph[node] else -1)
            if nnode >= 0:
                graph[nnode].remove(node)

            if values[node] % k == 0:
                res += 1
            else:
                values[nnode] += values[node]

            if nnode >= 0 and len(graph[nnode]) == 1:
                q.append(nnode)
        return res