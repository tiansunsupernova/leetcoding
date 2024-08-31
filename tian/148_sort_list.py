# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        mi = self.midpoint(head)
        l = self.sortList(head)
        r = self.sortList(mi)
        return self.merge(l, r)

    def midpoint(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        prev = None
        while head and head.next:
            prev = head if not prev else prev.next
            head = head.next.next
        mid = prev.next
        prev.next = None
        return mid

    def merge(self, h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
        if not h1: return h2
        if not h2: return h1
        prev = ListNode(0)
        cur = prev
        while h1 and h2:
            if h1.val < h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next
        cur.next = h1 if h1 else h2
        return prev.next

