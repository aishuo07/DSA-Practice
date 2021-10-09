class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def kmax(k):
            dic = defaultdict(int)
            j = 0
            s = 0
            for i in range(len(nums)):
                if dic[nums[i]]==0:
                    k-=1
                dic[nums[i]] += 1
                while k<0:
                    dic[nums[j]] -= 1
                    if dic[nums[j]] == 0:
                        k+=1
                    j+=1
                s+= i-j + 1
            print(s)
            return s
        return kmax(k)-kmax(k-1)