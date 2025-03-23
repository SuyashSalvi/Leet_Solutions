# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hm = defaultdict(list)
        q = deque()
        q.append((root, 0, 0))
        min_col = max_col = 0
        res = []

        while q:
            node, row, col = q.popleft()
            if node:
                hm[col].append((row, node.val))
                min_col = min(min_col, col)
                max_col = max(max_col, col)

                q.append((node.left, row + 1, col - 1))
                q.append((node.right, row + 1, col + 1))
        
        for col in range(min_col, max_col + 1):
            res.append([val for row, val in sorted(hm[col])])

        return res