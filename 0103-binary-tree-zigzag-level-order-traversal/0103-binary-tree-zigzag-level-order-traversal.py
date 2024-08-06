# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q, res, z = [root], [], 1
        while q:
            cur_level = []
            l = len(q)
            for i in range(l):
                n = q.pop(0)
                cur_level.append(n.val)
                
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            if z == 1:
                res.append(cur_level)
                z = -1
            else:
                res.append(cur_level[::-1])
                z = 1
        return res