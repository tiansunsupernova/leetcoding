"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def __init__(self):
        self.lastNode = None
    
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.traverse(head)
        if self.lastNode: self.lastNode.next = None

        return head


    # lastNode None. 1.  2. 3   7
    # node     1.    2   3. 7   8
    # tmp      None None 7. None 11
    
    def traverse(self, node):
        if node == None:
            return

        # [pre-order]
        tmp = node.child
        tmp2 = node.next
        node.child = None
        node.prev = self.lastNode

        if self.lastNode:
            self.lastNode.next = node
        self.lastNode = node

        self.traverse(tmp)
        self.traverse(tmp2)