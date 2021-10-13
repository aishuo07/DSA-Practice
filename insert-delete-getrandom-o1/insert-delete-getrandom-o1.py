class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.arr.append(val)
            self.dic[val]= len(self.arr)-1
            return True
        return False
    
    def remove(self, val: int) -> bool:
        if val in self.dic:
            self.arr[self.dic[val]], self.arr[-1], c = self.arr[-1], self.arr[self.dic[val]], self.arr[-1]
            self.dic[c] = self.dic[val]
            self.dic.pop(val)
            self.arr.pop()
            return True
        return False

    def getRandom(self) -> int:
        return self.arr[randrange(0, len(self.dic))-1]
    