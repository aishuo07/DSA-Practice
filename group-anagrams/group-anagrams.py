class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = ord('a')
        ans = defaultdict(list)
        for i in strs:
            arr = [0]*27
            for j in i:
                arr[ord(j)-a] += 1
            ans[' '.join(map(str, arr))].append(i)
        return ans.values()