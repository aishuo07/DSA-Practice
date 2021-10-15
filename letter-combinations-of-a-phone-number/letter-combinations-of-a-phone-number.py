class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dp = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno","7":"pqrs", "8":"tuv", "9":"wxyz"}
        ans = []
        def dfs(i, temp):
            if i == len(digits):
                if temp:
                    ans.append(temp)
                return 
            for j in dp[digits[i]]:
                dfs(i+1, temp + j)
        dfs(0, '')
        return ans