class Solution:
    def numPairsDivisibleBy60(self, time):
        time = Counter([i%60 for i in time])
        s = 0
        for i in time:
            if i<=30:
                if i == 0 or i ==30:
                    s += (time[i]*(time[i]-1))//2
                else:
                    s += time[i]*time[60-i]
        return s