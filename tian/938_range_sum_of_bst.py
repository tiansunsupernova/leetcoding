# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self, ):
        self.sum = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.traverse(root, low, high)
        return self.sum
    
    def traverse(self, node, low, high):
        if node is None: return
        self.traverse(node.left, low, high)
        if node.val >= low and node.val <= high:
            self.sum += node.val
        self.traverse(node.right, low, high)
