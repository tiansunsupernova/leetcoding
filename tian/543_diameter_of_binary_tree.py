# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxL = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.maxL

    def traverse(self, node) -> int:
        if node is None: return 0
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        self.maxL = max(self.maxL, left + right)
        return max(left, right) + 1
        