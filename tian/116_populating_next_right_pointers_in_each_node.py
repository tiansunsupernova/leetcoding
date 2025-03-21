"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque()
        if root: q.append(root)
        while q:
            l = len(q)
            prev = None
            for _ in range(l):
                node = q.popleft()
                if prev:
                    prev.next = node
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                prev = node
        return root