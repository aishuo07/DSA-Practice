class Solution:
    def numberOfRounds(self, startTime: str, endTime: str) -> int:
        c, d = int(startTime[:2])*60 + int(startTime[3:]), int(endTime[:2])*60 + int(endTime[3:])
        if c>d:
            d+=24*60
        return max(0, d//15 - (c+14)//15)
        