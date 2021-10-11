class LFUCache:
    def __init__(self, capacity):
        self.count = {}
        self.dic = OrderedDict()
        self.cap = capacity
        self.ind = 1
        
    def add(self, key, value, count):
        self.dic[key] = [count, value]
        if count in self.count:
            self.count[count][key] = None
        else:
            self.count[count] = OrderedDict()
            self.count[count][key] = None
            
    def remove(self, key):
        c, d = self.dic.pop(key)
        self.count[c].pop(key)
    
    def get(self, key):
        if key in self.dic:
            c, d = self.dic[key]
            self.remove(key)
            self.add(key, d, c + 1)
            return self.dic[key][1]
        return -1

    def put(self, key, value):
        if self.cap == 0:
            return
        if key in self.dic:
            c, d = self.dic[key]
            self.remove(key)
            self.add(key, value, c + 1)
        else:
            if len(self.dic)==self.cap:
                while not self.count[self.ind]:
                    self.ind += 1
                for i in self.count[self.ind]:
                    c = i
                    break
                self.remove(c)
                self.ind = 1
            self.add(key, value, 1)
        
                    
                    