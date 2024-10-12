"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def __init__(self):
        self.dummy = Node(-1)
        self.last = self.dummy
    
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return 
        self.traverse(root)
        self.last.right = self.dummy.right
        self.dummy.right.left = self.last
        return self.dummy.right

    def traverse(self, node):
        if node is None: return

        self.traverse(node.left)
        self.last.right = node
        node.left = self.last
        self.last = node
        self.traverse(node.right)