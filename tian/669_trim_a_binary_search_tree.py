# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None: return None
        l = self.trimBST(root.left, low, high)
        r = self.trimBST(root.right, low, high)
        if root.val < low: return r
        if root.val > high: return l
        root.left, root.right = l, r
        return root