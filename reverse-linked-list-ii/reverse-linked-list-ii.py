# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = ListNode(0, head)
        newh = curr
        i = 0
        new = None
        while i<left:
            i+=1
            new = curr
            curr = curr.next
        prev = None
        old = curr
        while i<=right:
            i+=1
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        new.next = prev
        old.next = curr
        return newh.next
            
            