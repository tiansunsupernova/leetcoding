# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        tree, idx = self.recur(s, 0)
        return tree

    def recur(self, s, i):
        if i == len(s):
            return None, i
        
        val, i = self.getNumber(s, i)
        node = TreeNode(val)

        if i < len(s) and s[i] == '(':
            node.left, i = self.recur(s, i + 1)
        
        if node.left and i < len(s) and s[i] == '(':
            node.right, i = self.recur(s, i + 1)
        
        index = i + 1 if i < len(s) and s[i] == ')' else i
        return node, index

    
    def getNumber(self, s, i):
        negative = False
        if s[i] == '-':
            negative = True
            i += 1
        val = 0
        while i < len(s) and s[i].isdigit():
            val = val * 10 + int(s[i])
            i += 1
        return -val if negative else val, i