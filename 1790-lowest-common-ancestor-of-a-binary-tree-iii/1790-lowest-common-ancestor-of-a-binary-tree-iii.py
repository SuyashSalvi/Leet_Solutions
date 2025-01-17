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
    # def get_depth(self, p):
    #     depth = 0
    #     while p:
    #         p = p.parent
    #         depth += 1
    #     return depth


    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
    #     pd = self.get_depth(p)
    #     qd = self.get_depth(q)

    #     for _ in range(pd - qd):
    #         p = p.parent
    #     for _ in range(qd - pd):
    #         q = q.parent

    #     while p != q:
    #         p = p.parent
    #         q = q.parent
        
    #     return p

        p1, p2 = q, p
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p

        return p1