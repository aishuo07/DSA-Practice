# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        ma = [0]
        def rec(root):
            if not root:
                return 0, 0
            c, c1 = rec(root.left)
            d, c2 = rec(root.right)
            ma[0] = max(ma[0], (c+d+root.val)/(c1+c2+1))
            return c+d+root.val, c1+c2 + 1
        rec(root)
        return ma[0]