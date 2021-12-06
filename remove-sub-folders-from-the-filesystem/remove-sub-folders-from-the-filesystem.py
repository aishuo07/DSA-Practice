class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        def add(i):
            root = trie
            flag = False
            for j in i.split('/'):
                if j not in root:
                    root[j] = {}
                    flag = True
                root = root[j]
                if not flag and 'end' in root:
                    return True
            root['end'] = True
        
        arr = []
        for i in sorted(folder):
            if not add(i):
                arr.append(i) 
        return arr