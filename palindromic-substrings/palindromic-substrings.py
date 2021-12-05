class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 1
        n = len(s)
        for i in range(1, n):
            j = i-1
            k = i+1
            while j>=0 and k<n and s[j] == s[k]:
                j-=1
                k+=1
                ans += 1
            j = i-1
            k = i
            while j>=0 and k<n and s[j] == s[k]:
                j-=1
                k+=1
                ans += 1
            ans += 1
        return ans