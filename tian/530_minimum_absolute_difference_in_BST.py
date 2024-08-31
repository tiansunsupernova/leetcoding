# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.last_val = None
        self.min_diff = float('inf')
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self._traverse(root)
        return self.min_diff
    
    def _traverse(self, node: Optional[TreeNode]):
        if not node: return
        self._traverse(node.left)
        if self.last_val != None:
            diff = node.val - self.last_val
            self.min_diff = min(self.min_diff, diff)
        self.last_val = node.val
        self._traverse(node.right)
