# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        if not l1:
            return l2
        if not l2:
            return l1
        head = node
        curr1 = l1
        curr2 = l2
        next1 = l1.next
        next2 = l2.next
        while curr1 or curr2:
            if not curr2 or (curr1 and curr2.val>curr1.val):
                node.next = curr1
                curr1 = next1
                if next1:
                    next1 = next1.next
            else:
                node.next = curr2
                curr2 = next2
                if next2:
                    next2 = next2.next
            node = node.next
        return head.next