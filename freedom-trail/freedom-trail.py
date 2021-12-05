class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        @cache
        def rec(ring, i):
            if i == len(key):
                return 0
            ans = float('inf')
            for j in range(len(ring)):
                if ring[j] == key[i]:
                    ans = min(ans, j + rec(ring[j:] + ring[:j], i+1), n-j + rec(ring[j:] + ring[:j], i+1))
            return ans
        return rec(ring, 0) + len(key)