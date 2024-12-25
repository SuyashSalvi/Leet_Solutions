class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # def find_farthest_node(n, adj, node):
            # q = deque([node])
            # visited = [False] * n
            # visited[node] = True

            # farthest_node = node
            # max_dist = 0
            # while q:
            #     for _ in range(len(q)):
            #         cur_node = q.popleft()
            #         farthest_node = cur_node

            #         for neigh in adj[cur_node]:
            #             if not visited[neigh]:
            #                 visited[neigh] = True
            #                 q.append(neigh)

            #     if q:
            #         max_dist += 1

            # return farthest_node, max_dist

        # def find_dia(n, adj):
        #     farthest_node, _ = find_farthest_node(n, adj, 0)
        #     _, dia = find_farthest_node(n,adj, farthest_node)
        #     return dia

        def find_dia(adj, node, parent):
            max_depth1 = max_depth2 = 0
            diameter = 0

            for neigh in adj[node]:
                if neigh == parent:
                    continue
                
                child_diameter, depth = find_dia(adj, neigh, node)
                depth += 1

                diameter = max(diameter, child_diameter)

                if depth > max_depth1:
                    max_depth2 = max_depth1
                    max_depth1 = depth
                elif depth > max_depth2:
                    max_depth2 = depth

            diameter = max(diameter, max_depth1 + max_depth2)
            return diameter, max_depth1


        n = len(edges1) + 1
        m = len(edges2) + 1

        adj1 = [[] for _ in range(n)]
        adj2 = [[] for _ in range(m)]

        for edge in edges1:
            adj1[edge[0]].append(edge[1])
            adj1[edge[1]].append(edge[0])

        for edge in edges2:
            adj2[edge[0]].append(edge[1])
            adj2[edge[1]].append(edge[0])

        # diameter1 = find_dia(n, adj1)
        # diameter2 = find_dia(m, adj2)
        diameter1,_ = find_dia(adj1, 0, -1)
        diameter2,_ = find_dia(adj2, 0, -1)

        diameter = ceil(diameter1/2)+ ceil(diameter2/2) + 1

        return max(diameter1, diameter2, diameter)

