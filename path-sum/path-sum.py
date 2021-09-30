# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        global ans
        ans = False
        def rec(root, s):
            global ans
            if not root:
                return 0
            if s+root.val == targetSum and root.left == None and root.right == None:
                ans = True
            rec(root.left, s+root.val)
            rec(root.right, s+root.val)
        rec(root, 0)
        return ans