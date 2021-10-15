class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def rec(i):
            if i == len(s):
                return 1
            if i> len(s):
                return 0
            a = 0
            if s[i] == '0':
                return 0
            if 0<int(s[i])<27:
                a += rec(i+1)
            if 0<int(s[i:i+2])<27:
                a+=rec(i+2)
            return a
        return rec(0)