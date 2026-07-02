class Solution:
    def insertAtBottom(self, st, item):
        # agar stack empty hai, to item ko yahin daal do (ye bottom ban jayega)
        if not st:
            st.append(item)
            return
        
        # warna top nikaalo, baaki recursively neeche daalo, phir top wapas rakho
        top = st.pop()
        self.insertAtBottom(st, item)
        st.append(top)
    def reverseStack(self, st):
        if st:
            top = st.pop()               # top nikaalo
            self.reverseStack(st)         # baaki stack ko reverse karo
            self.insertAtBottom(st, top)  # nikaale hue element ko bottom mein daalo
        
        return st
