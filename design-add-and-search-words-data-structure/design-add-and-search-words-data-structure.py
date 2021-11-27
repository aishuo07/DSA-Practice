class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        root = self.trie
        for i in word:
            if i not in root:
                root[i] = {}
            root = root[i]
        root['end'] = True

    def search(self, word):
        root = self.trie
        def rec(i, root):
            if i>=len(word) and 'end' in root:
                return True
            if i>=len(word):
                return False
            ans = False
            if word[i] == '.':
                for j in root:
                    if j!='end':
                        ans|=rec(i+1, root[j])
            elif word[i] in root:
                ans|=rec(i+1, root[word[i]])
            return ans
        return rec(0, root)
                    