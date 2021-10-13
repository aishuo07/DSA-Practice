class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dic = Counter(nums)
        self.q = deque([i for i in self.dic if self.dic[i] == 1])

    def showFirstUnique(self) -> int:
        while self.q and self.dic[self.q[0]]!=1:
            self.q.popleft()
        return self.q[0] if self.q else -1

    def add(self, value: int) -> None:
        self.dic[value] += 1
        if self.dic[value] == 1:
            self.q.append(value)
            
