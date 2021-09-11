# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        ans = deque()
        while q or root:
            if root:
                q.append(root)
                ans.appendleft(root.val)
                root = root.right
            else:
                root = q.pop().left
        return ans
                