"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q = deque([(root)])
        while q:
            lenQ = len(q)
            while lenQ > 0:
                node = q.popleft()
                if lenQ > 1:
                    node.next = q[0]
                lenQ -= 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root