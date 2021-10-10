class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        c0 = su = c1 = 0
        c0 = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                c0 += 1
            else:
                su += min(c0, c1)
                c1, c0 = c0, 1
        return su+min(c0, c1)