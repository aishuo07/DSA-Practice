class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        a = ord('a')
        ans = 0
        for i in range(0, 26):
            c = chr(a + i)
            start = -1
            co = set()
            cur = set()
            end = 0
            for i in range(len(s)):
                if s[i] == c:
                    if start == -1:
                        start = i
                    else:
                        end = i
                
            ans += len(set(s[start+1:end]))
        return ans