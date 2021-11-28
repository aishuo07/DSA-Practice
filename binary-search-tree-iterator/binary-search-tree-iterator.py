# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.q = []
        while root:
            self.q.append(root)
            root = root.left
        print(self.q)

    def next(self):
        c = self.q.pop()
        if c.right:
            temp = c.right
            while temp:
                self.q.append(temp)
                temp = temp.left
        return c.val
    
    def hasNext(self) -> bool:
        if self.q:
            return True
        return False
        