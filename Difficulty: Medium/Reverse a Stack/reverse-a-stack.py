class Solution:
    def reverseStack(self, st):
        # code here
        temp = []
    
        while st:
            temp.append(st.pop())   # ye ek hi reversal hai — ab temp reversed hai
        
        st.extend(temp)   # bas seedha copy kar do, dobara pop-push mat karo
        
        return st
