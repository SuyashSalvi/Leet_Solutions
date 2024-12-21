class Solution:
    def dfs(self, node, parent, adj,values, k, component_count):
        cur_sum = 0
        for nnode in adj[node]:
            if nnode != parent:
                cur_sum += self.dfs(nnode, node, adj, values, k, component_count)
                cur_sum %= k 
        
        cur_sum += values[node]
        cur_sum %= k

        if cur_sum == 0:
            component_count[0] += 1

        return cur_sum


    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        component_count = [0] #passing by refernce

        self.dfs(0, -1, adj, values, k, component_count)

        return component_count[0]