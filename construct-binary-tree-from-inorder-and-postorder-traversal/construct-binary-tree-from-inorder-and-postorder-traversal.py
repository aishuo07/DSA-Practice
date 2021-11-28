# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def rec(inorder):
            if postorder and postorder[-1] in inorder:
                root = TreeNode(postorder[-1])
                postorder.pop()
                ind = inorder.index(root.val)
                root.right = rec(inorder[ind+1:])
                root.left = rec(inorder[:ind])
                return root
        return rec(inorder)