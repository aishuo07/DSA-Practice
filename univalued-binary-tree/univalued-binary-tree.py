# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def rec(root):
            if not root:
                return True
            ans = True
            if root.left:
                if root.left.val != root.val:
                    return False
                ans&=rec(root.left)
            if root.right:
                if root.right.val != root.val:
                    return False
                ans&=rec(root.right)
            return ans
        return rec(root)
            