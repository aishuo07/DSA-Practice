class FreqStack:

    def __init__(self):
        self.freq = defaultdict(list)
        self.ma = defaultdict(int)
        self.c=0
        
    def push(self, val):
        self.ma[val]+=1
        self.freq[self.ma[val]].append(val)
        self.c = max(self.c, self.ma[val])
        
    def pop(self):
        c = self.freq[self.c].pop()
        self.ma[c]-=1
        if len(self.freq[self.c]) == 0:
            self.c-=1
        return c