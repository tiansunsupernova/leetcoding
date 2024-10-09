# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.di = defaultdict(list)
        self.left, self.right = 0, 0

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traverse(root, 0, 0)

        res = []
        for i in range(self.left, self.right + 1):
            col = sorted(self.di[i])
            res.append([v for i, v in col])
        return res
    
    def traverse(self, node, row, col):
        if node is None: return
        self.left = min(self.left, col)
        self.right = max(self.right, col)
        self.di[col].append((row, node.val))

        self.traverse(node.left, row + 1, col - 1)
        self.traverse(node.right, row + 1, col + 1)