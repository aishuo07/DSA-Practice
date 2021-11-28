# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if root:
            q.append(root)
        arr = []
        while q:
            arr.append([])
            for i in range(len(q)):
                c = q.popleft()
                arr[-1].append(c.val)
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
        return arr[::-1]