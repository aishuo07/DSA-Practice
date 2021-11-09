class Solution:
    def grayCode(self, n: int) -> List[int]:
        arr = [1<<i for i in range(n)]
        q = deque()
        dp = set()
        ans = []
        def rec(s):
            ans.append(s)
            dp.add(s)
            for i in arr:
                if s^i not in dp:
                    rec(s^i)
                    break
        rec(0)
        return ans