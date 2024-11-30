from collections import defaultdict, deque, Counter

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # 1 build graph and track in and out degrees
        adj_mat = defaultdict(deque)
        inD = Counter()
        outD = Counter()
        for s,e in pairs:
            adj_mat[s].append(e)
            outD[s] += 1
            inD[e] += 1

        # 2 find start node
        start_node = pairs[0][0]
        for node in outD:
            if inD[node] == outD[node] - 1:
                start_node = node
                break

        # 3 performing postorder DFS
        res = []
        def dfs(node):
            while adj_mat[node]:
                next_node = adj_mat[node].popleft()
                dfs(next_node)
            res.append(node)

        dfs(start_node)
        res.reverse()

        return [[res[i],res[i+1]] for i in range(len(res)-1)]