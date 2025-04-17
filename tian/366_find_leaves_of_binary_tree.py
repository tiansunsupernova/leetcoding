# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.di = defaultdict(list)

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        l = self.traverse(root)
        for i in range(1, l + 1):
            res.append(self.di[i])
        return res
    
    def traverse(self, node):
        if not node:
            return 0
        l = self.traverse(node.left)
        r = self.traverse(node.right)
        cur = max(l, r) + 1
        self.di[cur].append(node.val)
        return cur