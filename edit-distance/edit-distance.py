class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def rec(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            return min(1 + rec(i+1, j), rec(i+1, j+1) + (1 if word1[i] != word2[j] else 0), 1 + rec(i, j+1))
        return rec(0, 0)