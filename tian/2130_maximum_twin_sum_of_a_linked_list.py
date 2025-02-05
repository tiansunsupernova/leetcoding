# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        li = []
        fast, slow = ListNode(0), ListNode(0)
        fast.next, slow.next = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            li.append(slow.val)
        for i in range(len(li)- 1, -1, -1):
            slow = slow.next
            li[i] += slow.val
        return max(li)