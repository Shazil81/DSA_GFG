class Solution:
    def insertAtBottom(self,st,x):
        st2 = []
        
        while st:
            st2.append(st.pop())
        st2.append(x)
        
        while st2:
            st.append(st2.pop())
        
        return st
        