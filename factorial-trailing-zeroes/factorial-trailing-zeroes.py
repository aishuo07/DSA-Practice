class Solution:
    def trailingZeroes(self, n: int) -> int:
        t = 5
        ans = 0
        while n//t:
            ans += n//t
            t*=5
        return ans
            