# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(c, d):
            a, b = c.next, d.next
            root = ListNode()
            curr = root
            while c or d:
                if not c or(d and c.val>d.val):
                    curr.next = d
                    d = b
                    if b:
                        b = b.next
                else:
                    curr.next = c
                    c = a
                    if a:
                        a = a.next
                curr = curr.next
            return root.next
        def mergesort(head):
            if head:
                fast = head.next
                slow = head
                if head.next == None:
                    return head
                while fast and fast.next:
                    fast = fast.next.next
                    slow = slow.next
                t = slow.next
                slow.next = None
                return merge(mergesort(head), mergesort(t))
            return None
        return mergesort(head)