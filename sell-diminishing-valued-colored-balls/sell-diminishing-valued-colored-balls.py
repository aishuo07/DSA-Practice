class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        d = Counter(inventory)
        h = []
        ans = 0
        mod = 10**9 + 7
        def calc(n):
            return (n*(n+1))//2
        for i in d:
            heappush(h, [-i, d[i]])
        while h and orders>0:
            if len(h)>=2:
                c = heappop(h)
                d = heappop(h)
                if c[0] ==d[0]:
                    heappush(h, [c[0], c[1]+d[1]])
                else:
                    c[0] = abs(c[0])
                    d[0] = abs(d[0])
                    e = orders//c[1]
                    orders -= min(e, (c[0]-d[0]))*c[1]
                    ans = ans+(calc(c[0])-calc(c[0]-min(e, (c[0]-d[0]))))*c[1]
                    c[0] -= min(e, (c[0]-d[0]))
                    while orders>0 and c[0]>d[0]:
                        ans += min(orders, c[1])*c[0]
                        orders-=min(orders, c[1])
                        c[0]-=1
                    heappush(h, [-d[0], c[1]+d[1]])
            else:
                c = heappop(h)
                c[0] = abs(c[0])
                d = orders//c[1]
                orders -= d*c[1]
                ans = (ans+ (calc(c[0]) - calc(c[0]-d))*c[1])%mod
                c[0] -= d
                while orders>0 and c[0]>0:
                    ans = (ans + min(orders, c[1])*c[0])%mod
                    orders-=min(orders, c[1])
                    c[0]-=1
        return ans%mod
                