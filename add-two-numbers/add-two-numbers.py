# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        new = ListNode(0)
        head = new
        while l1 or l2:
            s = c
            if l1:
                s+=l1.val
                l1 = l1.next
            if l2:
                s+=l2.val
                l2 = l2.next
            if s>9:
                c = 1
            else:
                c = 0
            s%=10
            new.next = ListNode(s)
            new = new.next
        if c:
            new.next = ListNode(c)
        return head.next