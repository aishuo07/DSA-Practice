class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        if len(s1)>len(s2):
            return False
        d = Counter()
        for i in range(len(s1)):
            d[s2[i]] += 1
            
        for i in range(len(s1), len(s2)):
            if len([0 for i in 'abcdefghijklmnopqrstuvwxyz' if d[i] == c[i]]) == 26:
                return True
            d[s2[i-len(s1)]]-=1
            d[s2[i]] += 1
        if len([0 for i in 'abcdefghijklmnopqrstuvwxyz' if d[i] == c[i]]) == 26:
            return True
        return False