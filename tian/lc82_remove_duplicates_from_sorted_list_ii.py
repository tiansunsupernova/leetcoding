# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        di = {}
        cur = head
        while cur:
            v = cur.val
            di[v] = di.get(v, 0) + 1
            cur = cur.next
        
        cur = ListNode(0)
        res = cur
        cur.next = head

        while cur and cur.next:
            nxt = cur.next
            while nxt and nxt.val in di and di[nxt.val] > 1:
                nxt = nxt.next
            cur.next = nxt
            cur = cur.next
        return res.next if res.next else None

