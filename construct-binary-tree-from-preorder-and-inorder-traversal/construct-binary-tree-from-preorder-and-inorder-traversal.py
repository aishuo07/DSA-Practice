# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ind = [0]
        dic = {i:j for j, i in enumerate(inorder)}
        def rec(i, j):
            if ind[0]<len(preorder) and i<=dic[preorder[ind[0]]]<=j:
                root = TreeNode(preorder[ind[0]])
                ind[0] += 1
                root.left = rec(i, dic[root.val]-1)
                root.right = rec(dic[root.val] + 1, j)
                return root
        return rec(0, len(inorder)-1)