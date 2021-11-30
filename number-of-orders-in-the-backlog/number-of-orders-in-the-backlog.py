class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy = []
        sell = []
        for i in orders:
            if i[2] == 0:
                while sell and i[1] and sell[0][0]<=i[0]:
                    if sell[0][1]>i[1]:
                        sell[0][1]-=i[1]
                        i[1] = 0
                    else:
                        i[1]-=sell[0][1]
                        heappop(sell)
                if i[1]:
                    heappush(buy, [-i[0], i[1]])
            else:
                while buy and i[1] and -buy[0][0]>=i[0]:
                    if buy[0][1]>i[1]:
                        buy[0][1]-=i[1]
                        i[1] = 0
                    else:
                        i[1]-=buy[0][1]
                        heappop(buy)
                if i[1]:
                    heappush(sell, [i[0], i[1]])
        s = 0
        while buy or sell:
            s+= heappop(buy)[1] if buy else heappop(sell)[1]
        return s%(10**9 + 7)
            