class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        a = sorted(arr)
        s = Counter()
        s1 = Counter()
        c = 0
        for i in range(len(arr)):
            s[arr[i]] += 1
            s1[a[i]] += 1
            if s == s1:
                c+=1
        return c or 1