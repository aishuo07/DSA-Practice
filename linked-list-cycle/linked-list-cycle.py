# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=  head
        i = 0
        while curr:
            curr = curr.next
            i+=1
            if i>10**4:
                return True
        return False