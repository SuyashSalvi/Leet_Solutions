"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        last, first = None, None

        def helper(node):
            nonlocal first, last
            if node:
                # left
                helper(node.left)
                # node
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                # right
                helper(node.right)

        if not root:
            return None

        helper(root)

        # closing DLL
        first.left = last
        last.right = first
        return first