# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p: return not q
        if not q: return not p
        return (p.val == q.val and self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right))