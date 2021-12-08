
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        temp = root
        c = 0
        while temp:
            temp = temp.left
            c+=1
        def rec(root, l, r):
            if not root:
                return False
            if l == 0 and r == 0:
                return True
            if l<=r:
                return rec(root.right, l//2, r-l)
            else:
                return rec(root.left, l//2, r)
        l = 0
        r = 2**(c-1)
        if c == 1:
            return 1
        while l<=r:
            mid = (l+r)//2
            if rec(root, 2**(c-2), mid):
                l = mid+1
            else:
                r = mid - 1
        return  max(0, 2**(c-1)-1 + max(0, l if rec(root, 2**(c-2), l-1) else l-1))