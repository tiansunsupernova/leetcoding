# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return 0.0
        q = deque([root])
        res = []
        while q:
            size = len(q)
            total = 0
            for _ in range(size):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                total += node.val
            res.append(total / size)
        return res
