"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {}

        cur = head
        while cur:
            n = Node(x=cur.val)
            hm[cur] = n

            cur = cur.next
        
        cur = head
        while cur:
            c = hm[cur]
            c.next = hm[cur.next] if cur.next else None
            c.random = hm[cur.random] if cur.random else None
            cur = cur.next


        return None if len(hm) == 0 else hm[head]