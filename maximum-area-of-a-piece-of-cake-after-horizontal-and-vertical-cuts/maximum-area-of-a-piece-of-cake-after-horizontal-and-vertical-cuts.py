class Solution:
    def maxArea(self, h: int, w: int, hori, vert):
        hori = sorted(set(hori) | {h})
        prev = 0
        ma = 0
        for i in hori:
            ma = max(ma, i-prev)
            prev = i
        vert = sorted(set(vert) | {w})
        prev = 0
        ma1 = 0
        for i in vert:
            ma1 = max(ma1, i-prev)
            prev = i
        print(ma, ma1)
        return (ma*ma1)%(10**9 + 7)