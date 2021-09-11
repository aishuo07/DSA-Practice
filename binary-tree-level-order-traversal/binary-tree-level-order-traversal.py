class node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        head = node(root)
        count = 1
        curr = head
        level = []
        while head:
            co = 0
            level.append([])
            for i in range(count):
                if head.val.left:
                    curr.next = node(head.val.left)
                    curr = curr.next
                    co+=1
                if head.val.right:
                    curr.next = node(head.val.right)
                    curr = curr.next
                    co+=1
                level[-1].append(head.val.val)
                head = head.next
            count = co
        return level
            