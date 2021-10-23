class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(dict)
        c = defaultdict(int)
        maxc = 0
        for i in nums:
            if c[i] in count and i in count[c[i]]:
                count[c[i]].pop(i)
            c[i] += 1
            maxc = max(maxc, c[i])
            count[c[i]][i] = None
        ans = []
        while k>0:
            ans += list(count[maxc].keys())
            k -= len(count[maxc])
            maxc -=1
        return ans