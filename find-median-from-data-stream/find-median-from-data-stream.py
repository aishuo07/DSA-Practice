class MedianFinder:

    def __init__(self):
        self.mi = []
        self.ma = []
        self.n = 0

    def addNum(self, num: int) -> None:
        heappush(self.ma, num)
        if len(self.ma)>len(self.mi)+1:
            heappush(self.mi, -heappop(self.ma))
            
        while self.mi and -self.mi[0]>self.ma[0]:
            c = heappop(self.mi)
            d = heappop(self.ma)
            heappush(self.ma, -c)
            heappush(self.mi, -d)
        self.n+=1
            
    def findMedian(self) -> float:
        if self.n & 1:
            return self.ma[0]
        else:
            return (self.ma[0] -self.mi[0])/2