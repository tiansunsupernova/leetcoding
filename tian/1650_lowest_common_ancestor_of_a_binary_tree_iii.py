"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def __init__(self):
        self.parents = set()

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        while p is not None:
            self.parents.add(p)
            p = p.parent
        while q is not None:
            if q in self.parents: return q
            q = q.parent
        return None