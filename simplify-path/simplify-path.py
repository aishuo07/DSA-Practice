class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        temp = ''
        for i in path.split('/'):
            if not i or i== '.':
                continue
            elif i == '..':
                if st:
                    st.pop()        
            else:
                st.append(i)
        return '/' + '/'.join(st)
                