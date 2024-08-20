# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
        if not n1 and not n2: return True
        if (n1 and not n2) or (n2 and not n1): return False
        return n1.val == n2.val and self.isMirror(n1.left, n2.right) and self.isMirror(n2.left, n1.right)