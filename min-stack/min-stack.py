class MinStack:

    def __init__(self):
        self.arr = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if val<=self.min:
            self.arr.append(self.min)
            self.min = val
        self.arr.append(val)
    def pop(self):
        if self.arr[-1] == self.min:
            self.arr.pop()
            self.min = self.arr.pop()
        else:
            self.arr.pop()
    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min
