# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head

        oldhead = newhead = head
        
        l = 1
        while newhead.next:
            newhead = newhead.next
            l += 1
        
        k = k % l

        if k == 0: return oldhead
        newhead.next = oldhead

        
        newtail = head
        for _ in range(l - k - 1):
            newtail = newtail.next
        res = newtail.next
        newtail.next = None
        return res