# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        if not root: return 0
        q = deque([(root,0)])
        while q:
            size = len(q)
            for _ in range(size):
                node, cur = q.popleft()
                cur = cur * 10 + node.val
                if not node.left and not node.right: total+= cur
                if node.left: q.append((node.left, cur))
                if node.right: q.append((node.right, cur))
        return total

