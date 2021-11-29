class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        dic = defaultdict(int)
        s = ['0']*10
        res = 0
        dic['0000000000'] = 1
        for i in word:
            s[ord(i)-ord('a')] = str((int(s[ord(i)-ord('a')]) + 1)%2)
            t = ''.join(s)
            for j in range(10):
                temp = s[j]
                if s[j] == '1':
                    s[j] = '0'
                elif s[j] == '0':
                    s[j] = '1'
                res += dic[''.join(s)]
                s[j] = temp
            res += dic[t]
            dic[t] += 1
        return res