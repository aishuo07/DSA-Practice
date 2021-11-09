class Solution:
    def originalDigits(self, s: str) -> str:
        s = Counter(s)
        c0 = s['z']
        c6 = s['x']
        c8 = s['g']
        c7 = s['s'] - c6
        c5 = s['v'] - c7
        c4 = s['f'] - c5
        c3 = s['r'] - c4 - c0
        c2 = s['t'] - c3 - c8
        c1 = s['o'] - c0-c2-c4
        c9 = (s['n'] - c1 - c7)//2
        return '0'*c0 +'1'*c1 + '2'*c2 + '3'*c3 + '4'*c4 + '5'*c5 + '6'*c6 + '7'*c7 + '8'*c8 + '9'*c9
    