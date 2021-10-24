class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @cache
        def rec(i):
            if i >= len(s):
                return 1
            ans = 0
            if s[i] == '0':
                return 0
            for j in range(i+1, min(len(s)+1, i+3)):
                if s[i]!=0 and 0<int(s[i:j])<27:
                    ans+= rec(j)
            return ans
        return rec(0)