# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
    
        self.helper(root)
    
    def helper(self, node: Optional[TreeNode]) -> TreeNode:
        if not node or (not node.left and not node.right): return node
        if not node.left: return self.helper(node.right)
        prev_left = node.left
        prev_right = node.right
        left_tail = self.helper(prev_left)
        right_tail = self.helper(prev_right)
        if left_tail:
            left_tail.right = prev_right
            node.left = None
            node.right = prev_left
        return right_tail if right_tail else left_tail
