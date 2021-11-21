# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        while curr:
            n = dummy.next
            p = dummy
            next = curr.next
            curr.next = None
            while n and n.val<curr.val:
                n = n.next
                p = p.next
            if p.next!=curr:
                temp = p.next    
                p.next = curr
                curr.next = temp
            curr = next
        return dummy.next
            