# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        head = TreeNode()
        ro = [head]
        def rec(root):
            if not root:
                return
            ro[0].right = root
            ro[0] = root
            temp = root.right
            rec(root.left)
            root.left = None
            rec(temp)
        rec(root)
        return head