class LRUCache:

    def __init__(self, capacity):
        self.has = OrderedDict()
        self.cap = capacity
        
    def get(self, key):
        
        if key in self.has:
            val = self.has[key]
            self.has.pop(key)
            self.has[key] = val
            return val
        return -1
    
    def put(self, key, value):
        if key in self.has:
            self.has.pop(key)
            self.has[key] = value
        else:
            self.has[key] = value    
        if len(self.has) == self.cap+1:
            for i in self.has:
                self.has.pop(i)
                break