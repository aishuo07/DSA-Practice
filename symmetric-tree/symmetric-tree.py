class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def rec(left, right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            if left.val!=right.val:
                return False
            return rec(left.left, right.right) and rec(left.right, right.left)
        return rec(root.left, root.right)