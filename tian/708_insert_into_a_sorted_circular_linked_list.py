"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            res = Node(insertVal)
            res.next = res
            return res
        
        fast, slow = head, Node(-1)
        slow.next = fast

        while True:
            fast = fast.next
            slow = slow.next
            if (slow.val <= insertVal and fast.val >= insertVal) 
            or (slow.val > fast.val and (insertVal < fast.val or insertVal > slow.val)) 
            or fast == head:
                cur = Node(insertVal)
                slow.next = cur
                cur.next = fast
                return head