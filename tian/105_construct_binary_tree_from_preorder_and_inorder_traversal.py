# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.di = {}
        self.pi = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.di = {v: i for i, v in enumerate(inorder)}
        return self.construct(preorder, inorder, 0, len(preorder) - 1)
    
    def construct(self, preorder: List[int], inorder: List[int], p1: int, p2: int)  -> Optional[TreeNode]:
        if p1 > p2: return None
        root_val = preorder[self.pi]
        root = TreeNode(root_val)
        idx = self.di[root_val]
        
        self.pi += 1
        
        root.left = self.construct(preorder, inorder, p1, idx - 1)
        root.right = self.construct(preorder, inorder,idx + 1, p2)

        return root

