# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.di = {}

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.di = {v:i for i, v in enumerate(inorder)}
        return self.construct(inorder, postorder, 0, len(postorder) - 1)
    
    def construct(self, inorder: List[int], postorder: List[int], pi:int, pj:int) -> Optional[TreeNode]:
        if pi > pj: return None
        
        root_val = postorder.pop()
        root = TreeNode(root_val)
        in_idx = self.di[root_val]

        root.right = self.construct(inorder, postorder, in_idx + 1, pj)
        root.left = self.construct(inorder, postorder, pi, in_idx - 1)

        return root


