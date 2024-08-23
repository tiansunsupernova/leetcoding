# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        di = {root: None}
        queue = deque([root])

        while (p not in di) or q not in di:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    di[node.left] = node
                if node.right:
                    queue.append(node.right)
                    di[node.right] = node
        
        p_parents = set()
        while p:
            p_parents.add(p)
            p = di[p]
        
        while q:
            if q in p_parents: return q
            q = di[q]
        
        return root
            
                
