# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def buildGraph(node, parent):
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            if node.left:
                buildGraph(node.left, node)
            if node.right:
                buildGraph(node.right, node)
        
        buildGraph(root, 0)
        q = deque()
        q.append((target.val,0))
        visited = set([target.val]) 
        res = []
        while q:
            node, d = q.popleft()
            if d == k:
                res.append(node)
                continue
            for neigh in graph[node]:
                if neigh not in visited:
                    q.append((neigh, d + 1))
                    visited.add(neigh)
        return res