class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i in points:
            dic = DefaultDict(int)
            for j in points:
                dic[abs(i[0]-j[0])**2+ abs(i[1]-j[1])**2] += 1
            for i in dic:
                ans += dic[i]*(dic[i]-1)
        return ans