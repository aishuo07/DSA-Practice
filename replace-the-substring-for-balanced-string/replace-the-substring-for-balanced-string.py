class Solution:
    def balancedString(self, s: str) -> int:
        c = Counter(s)
        i, res, n = 0, float('inf'), len(s)
        for j in range(len(s)):
            c[s[j]] -= 1
            while i<n and all(n/4>=c[k] for k in 'QWER'):
                res = min(res, j-i+1)
                c[s[i]] += 1
                i+=1
        return res