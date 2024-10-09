# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        root = res = ListNode(0)

        for i, node in enumerate(lists):
            if node is not None: 
                heapq.heappush(h, (node.val, i, node))
        
        while h:
            val, i, node = heapq.heappop(h)
            root.next = ListNode(val)
            root = root.next
            if node.next is not None:
                node = node.next
                heapq.heappush(h, (node.val, i, node))
        
        return res.next
