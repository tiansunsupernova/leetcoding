# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root: return res
        
        q = deque([root])
        level = False
        while q:
            size = len(q)
            cur = deque()
            for _ in range(size):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                if level: 
                    cur.appendleft(node.val)
                else:
                    cur.append(node.val)
            res.append(list(cur))       
            level = not level
        return res

