class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        res = float('inf')
        for i in boxes:
            k = 0
            s = 0
            i.sort()
            for j in i:
                l = bisect.bisect(packages, j)
                s+=j*(l-k)
                k = l
            if l == len(packages):
                res = min(res, s)
        mod = 10**9 +  7
        return (res-sum(packages))%mod if res!=float('inf') else -1