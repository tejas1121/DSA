class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans=0
        st=[]
        
        for i in tokens:
            if i not in '+-/*':
                st.append(int(i))
            elif(len(st)>=2):
                
                if i=='+':
                    c=st.pop()
                    b=st.pop()
                    ans=c+b
                    st.append(ans)
                    
                elif i=='-':
                    c=st.pop()
                    b=st.pop()
                    ans=b-c
                    st.append(ans)
                elif i=='*':
                    c=st.pop()
                    b=st.pop()
                    ans=c*b
                    st.append(ans)            
                else:
                    c=st.pop()
                    b=st.pop()
                    ans=int(b/c)
                    st.append(ans)

        return st[-1]
            