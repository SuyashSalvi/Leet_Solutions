from collections import defaultdict, deque, Counter

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # 1 build graph and track in and out degrees
        adj_mat, inD, outD, res = defaultdict(deque), Counter(), Counter(), []
        for s,e in pairs:
            adj_mat[s].append(e)
            outD[s] += 1
            inD[e] += 1

        # 2 find start node
        start_node = next((node for node in outD if outD[node] == inD[node]+1),pairs[0][0])

        # 3 performing postorder DFS
        def dfs(node):
            while adj_mat[node]:
                dfs(adj_mat[node].popleft())
            res.append(node)

        dfs(start_node)
        return [[res[i],res[i-1]] for i in range(len(res)-1,0,-1)]