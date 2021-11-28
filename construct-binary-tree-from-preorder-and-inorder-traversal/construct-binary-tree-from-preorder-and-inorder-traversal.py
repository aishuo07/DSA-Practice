# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i = [0]
        def rec(inorder):
            if i[0]<len(preorder) and preorder[i[0]] in inorder:
                root = TreeNode(preorder[i[0]])
                ind = inorder.index(preorder[i[0]])
                i[0] += 1
                root.left = rec(inorder[:ind])
                root.right = rec(inorder[ind+1:])
                return root
        return rec(inorder)