"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        curr = head
        while curr:
            new = Node(curr.val)
            curr.next, new.next = new, curr.next
            curr = curr.next.next
        curr = head
        
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        curr = head.next
        while curr.next:
            curr.next = curr.next.next
            curr = curr.next
        return head.next