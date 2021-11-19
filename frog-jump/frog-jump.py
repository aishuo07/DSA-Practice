class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dic = {i:j for j, i in enumerate(stones)}
        @cache
        def rec(i, jump):
            if i == len(stones)-1:
                return True
            if jump<=0:
                return False
            ans = False
            if stones[i]+jump in dic:
                ans |= rec(dic[stones[i] + jump], jump)
            if stones[i] + jump - 1 in dic:
                ans |= rec(dic[stones[i] + jump-1], jump-1)
            if stones[i] + jump + 1 in dic:
                ans |= rec(dic[stones[i] + jump+1], jump+1)
            return ans
        if 1 not in dic:
            return False
        return rec(dic[1], 1)
        