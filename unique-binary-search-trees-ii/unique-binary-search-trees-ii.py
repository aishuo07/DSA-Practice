# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        ans = []
        def rec(l, r):
            res = []
            if l>r:
                return [None]
            for i in range(l, r+1):
                for j in rec(l, i-1):
                    for k in rec(i+1, r):
                        res.append(TreeNode(i, j, k))
            return res
        return rec(1, n)