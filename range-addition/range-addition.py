class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        self.arr = [0]*length
        for i in updates:
            self.arr[i[0]] += i[2]
            if i[1]+1<length:
                self.arr[i[1]+1] -=i[2]
        for i in range(1, length):
            self.arr[i] += self.arr[i-1]
        return self.arr