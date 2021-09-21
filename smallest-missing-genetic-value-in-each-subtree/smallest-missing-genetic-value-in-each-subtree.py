class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        arr = [[] for i in range(n)]
        for i in range(n):
            if parents[i] != -1:
                arr[parents[i]].append(i)
        vis = [0]*(10**5 + 10)
        def dfs(i):
            if vis[nums[i]] == 0:
                vis[nums[i]] = 1
                for j in arr[i]:
                    dfs(j)
        res = [1]*n
        try:
            ind = nums.index(1)
        except:
            return res
        ans = 1
        
        while ind!=-1:
            dfs(ind)
            while vis[ans] != 0:
                ans += 1
            res[ind] = ans
            ind = parents[ind]
        return res