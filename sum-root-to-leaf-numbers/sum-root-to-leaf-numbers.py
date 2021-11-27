# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        s = [0]
        def rec(root, t):
            if not root:
                return 
            if (root.left or root.right):
                rec(root.left, t*10 + root.val)
                rec(root.right, t*10 + root.val)
            else:
                s[0] += t*10 + root.val
        rec(root, 0)
        return s[0]