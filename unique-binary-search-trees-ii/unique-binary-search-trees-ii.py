# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def rec(l, r):
            if l>r:
                return [None]
            if l == r:
                return [TreeNode(l)]
            arr = []
            for i in range(l, r+1):
                left = rec(l, i-1)
                right = rec(i+1, r)
                for j in left:
                    for k in right:
                        root = TreeNode(i)
                        root.left = j
                        root.right = k
                        arr.append(root)
            return arr
        return rec(1, n)