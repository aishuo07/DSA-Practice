class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        def add(root, i):
            for j in i:
                if j not in root:
                    root[j] = {}
                root = root[j]
            root['end'] = True
        for i in dictionary:
            add(trie, i)
        def search(i):
            root = trie
            for k, j in enumerate(i):
                if j in root:
                    root = root[j]
                    if 'end' in root:
                        return i[:k+1]
                else:
                    break
            return ''
        ans = []
        for i in sentence.split(' '):
            c = search(i)
            if c:
                ans.append(c)
            else:
                ans.append(i)
        return ' '.join(ans)