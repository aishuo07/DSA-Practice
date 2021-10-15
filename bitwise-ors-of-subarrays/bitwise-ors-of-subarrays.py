class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        dp = set()
        x = 0
        old = set()
        old.add(arr[0])
        for i in arr[1:]:
            new = set()
            new.add(i)
            for j in old:
                new.add(j|i)
            dp|=old
            old = new
        dp|=old
        return len(dp)