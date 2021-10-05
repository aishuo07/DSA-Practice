class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0]*n
        def merge(a, b):
            i = j = 0
            nw = []
            while i<len(a) and j<len(b):
                if a[i][0]<=b[j][0]:
                    arr[a[i][1]] += j
                    nw.append(a[i])
                    i+=1
                else:
                    nw.append(b[j])
                    j+=1
            while i<len(a):
                arr[a[i][1]] += j
                nw.append(a[i])
                i+=1
            while j<len(b):
                nw.append(b[j])
                j+=1
            return nw
            
        def merges(l, r):
            if l<r:
                mid = (l+r)//2
                return merge(merges(l, mid), merges(mid+1, r))
            return [nums[l]]
        nums = [[i, j] for j, i in enumerate(nums)]
        merges(0, n-1)
        return arr