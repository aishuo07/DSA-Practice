class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        dic = Counter()
        arr = []
        arr.append(dic.copy())
        for i in nums:
            dic[i] += 1
            arr.append(dic.copy())
        ans = []
        for i in queries:
            c = arr[i[1]+1] - arr[i[0]]
            prev = float('-inf')
            ma = float('inf')
            for i in range(1, 101):
                if c[i]>0:
                    ma = min(ma, i-prev)
                    prev = i
            ans.append(ma if ma!=float('inf') else -1)
        return ans