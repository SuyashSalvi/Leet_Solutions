# class Solution:
#     def bfs(self,n,adj_list):
#         q = deque()
#         visited = [False] * n

#         q.append(0)
#         visited[0] = True

#         current_layer_nodes = 1
#         next_layer_nodes = 0
#         layer_count = 0

#         while q:
#             for _ in range(current_layer_nodes):
#                 cur_node = q.popleft()

#                 if cur_node == n-1:
#                     return layer_count

#                 for neigh in adj_list[cur_node]:
#                     if visited[neigh]:
#                         continue
#                     q.append(neigh)
#                     next_layer_nodes += 1
#                     visited[neigh] = True

#             current_layer_nodes = next_layer_nodes
#             next_layer_nodes = 0
#             layer_count += 1

#         return -1


#     def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
#         adj_list = [[] for _ in range(n)]
#         ans = []

#         for i in range(n-1):
#             adj_list[i].append(i+1)

#         for u, v in queries:
#             adj_list[u].append(v)
#             ans.append(self.bfs(n,adj_list))

#         return ans


class Solution:
    def dpTD(self,n,adj_list,cur_node,dp):
        if cur_node == n-1:
            return 0

        if dp[cur_node] != -1:
            return dp[cur_node]

        min_dist = n

        for neigh in adj_list[cur_node]:
            min_dist = min(min_dist, self.dpTD(n,adj_list,neigh,dp)+1)
        dp[cur_node] = min_dist
        return min_dist


    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        dp = [-1] * n
        adj_list = [[] for _ in range(n)]
        ans = []

        for i in range(n-1):
            adj_list[i].append(i+1)

        for u, v in queries:
            adj_list[u].append(v)
            ans.append(self.dpTD(n,adj_list,0,dp))
            print(dp,u,v)
            dp = [-1] * n

        return ans


         