class Solution:
    def uniqueLetterString(self, s: str) -> int:
        ans = 0
        arr = []
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            arr.append([-1, -1])
        print(arr)
        j = 0
        while j<len(s):
            i =ord(s[j]) - ord('A')
            print(i, len(arr))
            print(arr[i])
            ans += (j-arr[i][1])*(arr[i][1] - arr[i][0])
            arr[i][0], arr[i][1] = arr[i][1], j
            j+=1
        for i in arr:
            if i[1]!=-1:
                ans += (len(s) - i[1])*(i[1]-i[0])
        return ans