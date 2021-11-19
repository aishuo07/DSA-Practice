class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = product = 1
        a = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for i in range(n):
            product*= a[i]
            ans += product
        return ans