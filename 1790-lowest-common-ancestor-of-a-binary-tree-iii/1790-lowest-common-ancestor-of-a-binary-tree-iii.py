"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def depth(node):
            d = 0
            while node:
                node = node.parent
                d += 1
            return d

        depth_p = depth(p)
        depth_q = depth(q)

        while depth_p > depth_q:
            depth_p -= 1
            p = p.parent
        while depth_q > depth_p:
            depth_q -= 1
            q = q.parent

        while p != q:
            q = q.parent
            p = p.parent
        return p