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
    def connect(self, root: 'Node') -> 'Node':
        q = deque()
        if not root: return None
        q.append(root)

        while q:
            size = len(q)
            prev = None
            for i in range(size):
                node = q.popleft()
                if prev:
                    prev.next = node
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                prev = node
        return root
                

