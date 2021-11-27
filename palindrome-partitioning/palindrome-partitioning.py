class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def rec(i, temp):
            if i>= len(s):
                ans.append(temp)
            t = ''
            for j in range(i, len(s)):
                t += s[j]
                if t == t[::-1]:
                    rec(j+1, temp + [t])
        rec(0, [])
        return ans