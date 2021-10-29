class Solution:
    def numberOfWeeks(self, arr):
        return min(2*(sum(arr)-max(arr))+1, sum(arr))