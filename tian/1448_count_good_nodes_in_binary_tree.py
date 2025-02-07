# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cnt = 0

    def traverse(self, node, curmax):
        if not node: return
        if node.val >= curmax:
            self.cnt += 1
            curmax = node.val
        self.traverse(node.left, curmax)
        self.traverse(node.right, curmax)

    def goodNodes(self, root: TreeNode) -> int:
        self.traverse(root, float('-inf'))
        return self.cnt

        