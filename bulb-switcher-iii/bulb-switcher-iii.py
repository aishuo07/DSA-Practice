class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        s = [0]*(len(light)+1)
        j = 1
        count = 0
        for i in range(len(light)):
            s[light[i]] = 1
            while j<len(light) and s[j] == 1:
                j+=1
            if j == i+2 or j>=len(light):
                count+=1
        return count