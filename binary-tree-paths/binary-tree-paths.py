# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def rec(root, temp):
            if not root:
                return 
            if root.left == None and root.right==None:
                ans.append(temp + str(root.val))
                return
            rec(root.left, temp + str(root.val) + '->')
            rec(root.right, temp + str(root.val) + '->')
        rec(root, '')
        return ans