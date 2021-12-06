# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def rec(root, path, s):
            if not root:
                return 
            if (root.left or root.right):
                rec(root.left, path + [root.val], s+root.val)    
                rec(root.right, path + [root.val], s+root.val)
            else:
                if s + root.val ==targetSum:
                    ans.append(path + [root.val])
        rec(root, [], 0)
        return ans