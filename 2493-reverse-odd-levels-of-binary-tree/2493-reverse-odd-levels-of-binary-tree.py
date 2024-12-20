# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left_child, right_child, level):
            if left_child == None or right_child == None:
                return
            # if the next level is odd, need to interchange their node values
            if level % 2 == 0:
                left_child.val, right_child.val = right_child.val, left_child.val
            dfs(left_child.left, right_child.right, level + 1)
            dfs(left_child.right, right_child.left, level + 1)

        dfs(root.left, root.right, 0)
        return root