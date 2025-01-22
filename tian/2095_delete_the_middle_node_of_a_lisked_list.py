# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 2 3 4  - 00 12 24 
        # 1 2 3 4 5 - 00 12 24
        if not head or not head.next: return None
        fast, slow = ListNode(), ListNode()
        fast.next, slow.next = head, head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        return head