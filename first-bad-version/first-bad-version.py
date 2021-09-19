# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        l= 0
        r = n-1
        while l<=r:
            mid = (l+r)//2
            if isBadVersion(mid):
                r = mid-1
            else:
                l = mid+1
        return l