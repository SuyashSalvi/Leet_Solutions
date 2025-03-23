# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def build_graph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur)

        build_graph(root, 0)

        res = []
        visited = set([target.val])
        q = deque([(target.val, 0)])
        while q:
            cur, dist = q.popleft()
            if dist == k:
                res.append(cur)
                continue
            for neigh in graph[cur]:
                if neigh not in visited:
                    q.append((neigh, dist + 1))
                    visited.add(neigh)
        return res