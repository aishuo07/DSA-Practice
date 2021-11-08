"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):
        curr = head
        if not head:
            return 
        while curr:
            node = Node(curr.val)
            next = curr.next
            curr.next = node
            node.next = next
            curr = next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        curr = head.next
        while curr and curr.next:
            next = curr.next.next
            curr.next = next
            curr = next
        return head.next