# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.last = None
        self.res = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.traverse(root)
        return self.res

    def traverse(self, root: Optional[TreeNode]):
        if not root: return
        self.traverse(root.left)
        if self.last != None and self.last >= root.val:
            self.res = False
        self.last = root.val
        self.traverse(root.right)