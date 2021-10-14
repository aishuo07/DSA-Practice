class Solution:
    def calculate(self, s: str) -> int:
        st = []
        def func(c, d, op):
            if op == '/':
                return int(d/c)
            elif op == '+':
                return c+d
            elif op == '*':
                return c*d
            else:
                return d-c
        def precedence(current_op, op_from_ops):
            if op_from_ops == "(" or op_from_ops == ")":
                return False
            if (current_op == "*" or current_op == "/") and (op_from_ops == "+" or op_from_ops == "-"):
                return False
            return True
        op = []
        
        n = len(s)
        j = 0
        while j<n:
            i = s[j]
            if i.isdigit():
                num = 0
                while j<n and s[j].isdigit():
                    num = num*10 + int(s[j])
                    j+=1
                st.append(num)
            elif i =='(':
                op.append(i)
                j+=1
            elif i == ')':
                while op and op[-1]!='(':
                    c = st.pop()
                    d = st.pop()
                    st.append(func(c, d, op.pop()))
                op.pop()
                j+=1
            elif i in ["+", "-", "/", "*"]:
                while op and precedence(i, op[-1]):
                    c = st.pop()
                    d = st.pop()
                    st.append(func(c, d, op.pop()))
                op.append(i)
                j+=1
        while op:
            c = st.pop()
            d = st.pop()
            st.append(func(c, d, op.pop()))
        return int(st[-1])