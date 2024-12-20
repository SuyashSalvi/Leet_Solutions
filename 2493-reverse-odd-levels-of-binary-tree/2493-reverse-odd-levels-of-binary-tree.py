# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        level = 0

        while q:
            cur_q_size = len(q)
            cur_level_nodes = []

            for _ in range(cur_q_size):
                node = q.pop(0)
                if level % 2 == 1:
                    cur_level_nodes.append(node)
                if node.left:
                    q.append(node.left)
                    q.append(node.right)
                
            if level % 2 == 1:
                left, right = 0, len(cur_level_nodes) - 1
                while left < right:
                    cur_level_nodes[left].val, cur_level_nodes[right].val = cur_level_nodes[right].val, cur_level_nodes[left].val
                    left += 1
                    right -= 1
            level += 1
        return root