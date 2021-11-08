class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr = [1<<i for i in range(32)]
        ans = [0 for _ in range(32)]
        for i in nums:
            for k, j in enumerate(arr):
                if abs(i)&j != 0:
                    ans[k] = (ans[k] + 1)%3
        res = 0
        for i in range(32):
            if ans[i] == 1:
                res += arr[i]
        return res if nums.count(res) == 1 else -res
                