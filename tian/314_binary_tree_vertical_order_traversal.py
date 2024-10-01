# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# Doesn't work with Example 3
    # def __init__(self):
    #     self.di = defaultdict(list)
    #     self.minx = float('inf')
    #     self.maxx = float('-inf')

    # def dfs(self, node, x):
    #     if not node:
    #         return
        
    #     self.minx = min(self.minx, x)
    #     self.maxx = max(self.maxx, x)
    #     self.di[x].append(node.val)
    #     self.dfs(node.left, x-1)
    #     self.dfs(node.right, x+1)
    
    # def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     self.dfs(root, 0)
    #     res = []
    #     for i in range(self.minx, self.maxx + 1):
    #         res.append(self.di[i])
    #     return res
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        di = defaultdict(list)
        res = []
        minx = 0
        maxx = 0
        if root is None: return res

        q = deque([(root, 0)])
        while q:
            node, x = q.popleft()
            minx = min(x, minx)
            maxx = max(x, maxx)
            di[x].append(node.val)
            if node.left is not None: q.append((node.left, x - 1))
            if node.right is not None: q.append((node.right, x + 1))
        
        for i in range(minx, maxx + 1):
            res.append(di[i])
        return res

                        

