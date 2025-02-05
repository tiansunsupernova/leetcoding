# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 1
        oddhead, evenhead = ListNode(0), ListNode(0)
        odd, even = oddhead, evenhead
        
        while head:
            if cnt % 2 == 1:
                oddhead.next = head
                oddhead = oddhead.next
            else:
                evenhead.next = head
                evenhead = evenhead.next
            
            head = head.next
            cnt += 1
        oddhead.next = even.next
        evenhead.next = None
        return odd.next


# head 1 2 3 4 5
# oddhead 0 - 1 - 3 - 5
# evenhead 0 - 2 - 4
# cnt 2 3 4
        

