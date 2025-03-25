# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None

        def helper(i):
            sign = 1
            if s[i] == '-':
                sign = -1
                i += 1
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            node = TreeNode(num * sign)

            if i < len(s) and s[i] == '(':
                i += 1
                node.left, i = helper(i)
                i += 1

            if i < len(s) and s[i] == '(':
                i += 1
                node.right, i = helper(i)
                i += 1
            return node, i

        root, _ = helper(0)
        return root