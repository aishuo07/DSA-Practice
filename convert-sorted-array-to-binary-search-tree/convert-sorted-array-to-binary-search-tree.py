# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(l, r):
            if l > r:
                return
            mid = (l+r)//2
            root = TreeNode(nums[mid])
            root.left = rec(l, mid-1)
            root.right = rec(mid+1, r)
            return root    
        return rec(0, len(nums)-1)