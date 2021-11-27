class Solution:
    def minCut(self, s: str) -> int:
        arr = [float('inf')]*len(s) + [0]
        arr[0] = 0
        if s == s[::-1]:
            return 0
        for i in range(len(s)):
            for j in range(i+1):
                if s[j:i+1] == s[j:i+1][::-1]:
                    if j == 0:
                        arr[i] = 0
                    else:
                        arr[i] = min(arr[j-1] + 1, arr[i])
        print(arr)
        return arr[-2]