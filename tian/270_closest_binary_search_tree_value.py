# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        node = root
        res = node.val
        while node:
            if abs(res - target) > abs(node.val - target):
                res = node.val
            elif abs(res - target) == abs(node.val - target):
                res = node.val if node.val < res else res
            node = node.left if target <= node.val else node.right
        return res