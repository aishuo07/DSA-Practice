# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(head):
            if not head or not head.next:
                return head
            prev = head
            curr = head.next
            next = curr.next
            curr.next = prev
            prev.next = rec(next)
            return curr
        
        return rec(head)