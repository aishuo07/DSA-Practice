class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        res = ''
        taken = False
        for j, i in enumerate(num):
            if int(i)>change[int(i)] and taken:
                res += num[j:]
                return res
            elif int(i)<change[int(i)]:
                res += str(change[int(i)])
                taken = True
            elif taken and int(i) == change[int(i)]:
                res += i
            else:
                res += i
        return res