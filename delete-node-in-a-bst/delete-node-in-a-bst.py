# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def rec(root):
            if not root:
                return 
            if root.val<key:
                root.right = rec(root.right)
            elif root.val>key:
                root.left = rec(root.left)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                prev = root
                temp = root
                root = root.left
                while root and root.right:
                    prev = root
                    root = root.right
                if root:
                    te = root.left
                else:
                    te = None
                if root:
                    root.left = temp.left
                    root.right = temp.right
                if root and prev == temp:
                    root.left = te
                elif prev:
                    prev.right = te
            return root
        return rec(root)