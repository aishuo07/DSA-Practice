class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def rec(i):
            if i>=len(s):
                return 1
            if s[i]=='0':
                return 0
            tmp = ''
            ans = 0
            for j in range(i, min(i+2, len(s))):
                tmp += s[j]
                if 0<int(tmp)<27:
                    ans += rec(j+1)
            return ans
        return rec(0)