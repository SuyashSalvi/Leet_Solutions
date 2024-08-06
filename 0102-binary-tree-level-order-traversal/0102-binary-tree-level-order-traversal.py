# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q, res = [root], []
        while(q):
            l = len(q)
            cur_level = []

            for i in range(l):
                n = q.pop(0)
                cur_level.append(n.val)

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            res.append(cur_level)
        return res
