# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        columnTable = defaultdict(list)
        q = deque([(root,0)])
        minCol, maxCol = 0, 0

        while q:
            node, col = q.popleft()
            if node is not None:
                columnTable[col].append(node.val)
                minCol = min(minCol,col)
                maxCol = max(maxCol,col)

                q.append((node.left,col-1))
                q.append((node.right,col+1))

        return [columnTable[x] for x in range(minCol, maxCol+1)]