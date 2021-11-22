class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(int)
        for j, i in enumerate(nums):
            if i in dic:
                if j-dic[i]<=k:
                    return True
            dic[i] = j
        return False