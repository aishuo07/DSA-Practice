# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        def rec(root):
            if not root:
                return ''
            return str(root.val) + '(' + rec(root.left) + ')' + '(' + rec(root.right) + ')'             
        return rec(root)
    
    def deserialize(self, data):
        i = [0]
        def rec():
            if i[0]>=len(data):
                return 
            s = ''
            while i[0]<len(data) and data[i[0]].isdigit():
                s+=data[i[0]]
                i[0] += 1
            if not s:
                return 
            root = TreeNode(s)
            i[0] += 1
            root.left = rec()
            i[0] += 2
            root.right = rec()
            i[0] += 1
            return root
        return rec()
            