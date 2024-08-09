# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = [[root.val]]
        while q:
            len_q = len(q)
            cur_level = []
            for _ in range(len_q):
                node = q.popleft()
                if node.left:
                    cur_level.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    cur_level.append(node.right.val)
                    q.append(node.right)
            if cur_level:
                ans.append(cur_level)
        return ans[::-1]