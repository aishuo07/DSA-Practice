class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dic = Counter(nums)
        ans = []
        def rec(temp):
            if not dic:
                if temp not in ans:
                    ans.append(temp)
                return 
            for i in dic.copy():
                dic[i] -= 1
                if dic[i] == 0:
                    dic.pop(i)
                rec(temp + [i])
                dic[i] += 1
        rec([])   
        return ans