class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        st = [float('inf')]
        ans = 0
        for i in arr:
            while i>=st[-1]:
                c = st.pop()
                ans += c*min(i, st[-1])
            st.append(i)
        while len(st)>2:
            ans += st.pop()*st[-1]
        return ans
            