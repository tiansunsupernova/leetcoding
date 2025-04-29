# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(lo = float('-inf'),  hi = float('inf')):
            nonlocal idx
            if idx == len(preorder):
                return None
            val = preorder[idx]
            if val < lo or val > hi:
                return None
            idx += 1
            root = TreeNode(val)
            root.left = helper(lo, val)
            root.right = helper(val, hi)
            return root

        idx = 0
        return helper()