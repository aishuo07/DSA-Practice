class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = Counter(arr)
        j = 1
        for i in sorted(rank.keys()):
            rank[i] = j
            j+=1
        ans  =[]
        for i in arr:
            ans.append(rank[i])
        return ans