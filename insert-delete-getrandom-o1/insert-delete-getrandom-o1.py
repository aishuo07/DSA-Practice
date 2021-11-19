import random

class RandomizedSet:

    def __init__(self):
        self.s = []
        self.dic = {}

    def insert(self, val: int):
        if val not in self.dic:
            self.s.append(val)
            self.dic[val] = len(self.s)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dic:
            self.dic[self.s[-1]] = self.dic[val]
            self.s[self.dic[val]], self.s[-1] = self.s[-1], self.s[self.dic[val]]
            self.s.pop()
            self.dic.pop(val)
            return True
        return False
    def getRandom(self) -> int:
        return random.choice(self.s)