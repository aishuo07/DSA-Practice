class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = {}
        products.sort()
        for i in products:
            trie = root
            for j in i:
                if 'end' in trie:
                    if len(trie['end'])<3:
                        trie['end'].append(i)
                else:
                    trie['end'] = [i]
                if j not in trie:
                    trie[j] = {}    
                trie = trie[j]
            if 'end' in trie:
                if len(trie['end'])<3:
                    trie['end'].append(i)
            else:
                trie['end'] = [i]
        ans = []
        trie = root
        flag = True
        for i in searchWord:
            if i in trie and flag:
                trie = trie[i]
                ans.append(trie['end'])
            else:
                flag = False
                ans.append([])
        return ans