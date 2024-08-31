# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        node = res
        c = 0
        while l1 or l2:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            cur = (c + v1 + v2) % 10
            c = (c + v1 + v2) // 10
            node.next = ListNode(cur)
            node = node.next
        if c == 1:
            node.next = ListNode(1)
            node = node.next
        return res.next