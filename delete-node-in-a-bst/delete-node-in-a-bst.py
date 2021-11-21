# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def rec(root, key):
            if not root:
                return 
            if root.val<key:
                root.right = rec(root.right, key)
            elif root.val>key:
                root.left = rec(root.left, key)
            else:
                if not (root.left and root.right):
                    return root.left or root.right
                temp = root.right
                while temp and temp.left:
                    temp = temp.left
                root.val = temp.val
                key = root.val
                root.right = rec(root.right, key)
            return root
        return rec(root, key)
        
                    