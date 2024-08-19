"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        
        di = {} # key = OldNode value = NewNode
        copy = head

        while head:
            di[head] = Node(head.val)
            head = head.next

        head = copy
        
        while head:
            di[head].next = di.get(head.next)
            di[head].random = di.get(head.random)
            head = head.next
        return di[copy]
