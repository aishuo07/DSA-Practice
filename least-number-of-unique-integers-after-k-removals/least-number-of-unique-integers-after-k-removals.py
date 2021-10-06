class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = Counter(arr)
        c = sorted(dic.values())
        i = 0
        while i<len(c):
            if c[i]<=k:
                k-=c[i]
            else:
                break
            i+=1
        return len(c)-i