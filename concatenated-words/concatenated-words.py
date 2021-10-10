class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set()
        res = []
        words.sort(key = lambda x:len(x))
        for i in words:
            dp = [0]*len(i) + [1]
            for j in range(-1, len(i)):
                s = ''
                if dp[j]:
                    for k in range(j+1, len(i)):
                        s += i[k]
                        if s in d:
                            dp[k] = 1
            if len(i)>=2 and dp[-2]:
                res.append(i)
            d.add(i)
        return res