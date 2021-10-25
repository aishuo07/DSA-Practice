class trie:
    
    def __init__(self):
        self.child = defaultdict(trie)
        self.end = False

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key = lambda x:len(x))
        root = trie()
        ans = []

        def search(i):
            temp = root
            if not i:
                return True
            ans = False
            if i in dp:
                return dp[i]
            for k, j in enumerate(i):
                if j in temp.child:
                    temp = temp.child[j]
                    if temp.end:
                        ans |= search(i[k+1:])
                else:
                    dp[i] = ans
                    return ans
            dp[i]= ans
            return ans
        
        for i in words:
            temp = root
            dp = {}
            if search(i) and i!='':
                ans.append(i)
            for j in i:
                temp = temp.child[j]
            temp.end = True
            
        return ans