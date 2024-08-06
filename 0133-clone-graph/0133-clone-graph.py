"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return node
        
        q, c = deque([node]), {node.val: Node(node.val)}
        while q:
            cur = q.popleft()
            cur_clone_node = c[cur.val]

            for n in cur.neighbors:
                if n.val not in c:
                    c[n.val] = Node(n.val)
                    q.append(n)
                cur_clone_node.neighbors.append(c[n.val])

        return c[node.val]