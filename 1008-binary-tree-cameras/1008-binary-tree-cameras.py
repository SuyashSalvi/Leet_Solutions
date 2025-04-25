# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # NOT COVERED - 0
        # COVERED - 1
        # HAS CAMERA - 2
        def dfs(node):
            # An empty child is trivially covered and uses 0 cameras
            if not node:
                return 1, 0
            
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            cams = lc + rc

            # If either child is not covered, we must place a camera here
            if ls == 0 or rs == 0:
                return 2, cams + 1

            # If any child has a camera, then we're covered
            if ls == 2 or rs == 2:
                return 1, cams

            # Otherwise, we're not covered (and defer coverage to our parent)
            return 0, cams

        root_state, total_cams = dfs(root)
        # If the root itself remains uncovered, add one more camera
        return total_cams + 1 if root_state == 0 else total_cams