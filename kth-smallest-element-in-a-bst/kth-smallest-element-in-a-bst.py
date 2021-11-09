# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        ans = [k, True]
        def rec(root):
            if not root:
                return
            
            rec(root.left)
            if ans[1]:
                ans[0] -= 1
            if ans[0] == 0 and ans[1]:
                ans[0] = root.val
                ans[1] = False
            rec(root.right)
        rec(root)
        return ans[0]