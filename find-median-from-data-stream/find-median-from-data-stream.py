class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []
        self.num = 0
    def addNum(self, num):
        heappush(self.high, num)
        if len(self.low)+1<len(self.high):
            c = -heappop(self.high)
            heappush(self.low, c)
        while self.low and self.high and -self.low[0]>self.high[0]:
            c = -heappop(self.low)
            d = -heappop(self.high)
            heappush(self.low, d)
            heappush(self.high, c)
        self.num += 1
        

    def findMedian(self):
        if self.num & 1:
            return self.high[0]
        else:
            return (-self.low[0] + self.high[0])/2 