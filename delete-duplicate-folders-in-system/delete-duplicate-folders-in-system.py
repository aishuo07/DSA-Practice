class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.dele = False
        
        
class Solution:
    def deleteDuplicateFolder(self, paths):
        root = Node()
        paths.sort()
        count = defaultdict(list)
        for i in paths:
            temp = root
            for j in i:
                temp = temp.child[j]
        def dfs(root):
            ans = '('
            for i in root.child:
                ans+= i+dfs(root.child[i])
            ans += ')'
            if ans != '()':
                count[ans].append(root)
            return ans
        dfs(root)
        for i in count:
            if len(count[i])>1:
                for j in count[i]:
                    j.dele = True
        ans = []
        print(count)
        def dfs1(root, path):
            for i in root.child:
                if not root.child[i].dele:
                    dfs1(root.child[i], path + [i])
            if path:
                ans.append(path)
        dfs1(root,[])
        return ans
                
            
                    