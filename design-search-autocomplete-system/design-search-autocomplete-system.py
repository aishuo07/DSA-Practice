class MyString:
    def __init__(self, word):
        self.word = word

    def __lt__(self, other):
        return self.word > other.word

    def __eq__(self, other):
        return self.word == other.word


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = {}
        k = 0
        for i in zip(sentences, times):
            self.add(i[0], i[1])
        self.str = ''
        self.var = self.root
        self.bool = True
        
    def add(self, word, time):
        trie = self.root
        for j in word:
            if j not in trie:
                trie[j] = {'end' : 0}
            trie = trie[j]
        trie['end'] += time
        
    def find(self, st):
        h = []
        if not self.bool:
            return []
        def dfs(trie, temp):
            if trie['end']!=0:
                heappush(h, [trie['end'], MyString(temp)])
                if len(h)>3:
                    heappop(h)
            for i in trie:
                if i!='end':
                    dfs(trie[i], temp+i)
        for c in st:
            if c in self.var:
                self.var = self.var[c]
                trie = self.var
            else:
                self.bool = False
                break
        if not self.bool:
            return []
        dfs(trie, self.str)
        l = []
        while h:
            l.append(heappop(h)[1].word)
        return l[::-1]
        
        
    def input(self, c):
        if c[-1] == '#':
            self.add(self.str + c[:-1], 1)
            self.var = self.root
            self.str = ''
            self.bool = True
            return []
        else:
            self.str += c
            return self.find(c)