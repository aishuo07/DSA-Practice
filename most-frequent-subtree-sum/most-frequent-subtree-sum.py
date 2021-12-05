# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        dp = defaultdict(int)
        def rec(root):
            if not root:
                return 0
            c = root.val + rec(root.left) + rec(root.right)
            dp[c]  += 1
            return c
        rec(root)
        m = max(dp.values())
        return [i for i in dp if dp[i] == m]