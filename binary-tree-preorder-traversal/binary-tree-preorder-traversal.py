class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        arr = []
        while curr:
            if not curr.left:
                arr.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right and pre.right!=curr:
                    pre = pre.right
                if pre.right == None:
                    arr.append(curr.val)
                    pre.right = curr
                    curr = curr.left
                elif pre.right == curr:
                    curr = curr.right
                    pre.right = None
        return arr
                
                    
                    
                    