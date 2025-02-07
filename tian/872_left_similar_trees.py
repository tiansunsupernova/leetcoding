# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node) -> TreeNode:
        if node:
            if not node.left and not node.right:
                yield(node.val)
            else:
                yield from self.dfs(node.left)
                yield from self.dfs(node.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = list(self.dfs(root1))
        l2 = list(self.dfs(root2))
        return l1 == l2