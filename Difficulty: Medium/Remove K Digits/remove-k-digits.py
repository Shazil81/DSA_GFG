class Solution:
    def removeKdig(self, s, k):
        # code here
        # Stack + Greedy: Optimal one
        stack = []

        for digit in s:
            # Agar stack ka element bada ho jaye aane wale digit se to hm pop krenge tb tk jab condition n fail ho jaye(Monotonic Increasing stack)
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            
            stack.append(digit)
        # Maan Lo number hi ascending order me ho K to bach jayega tab kya krna hai reverse order me se hta dena jo htane k baad aayega wohi mera sab se chhota hoga
        while k > 0:
            stack.pop()
            k -= 1
        
        res = "".join(stack).lstrip("0") # ye leading zeros htane k liye

        return res or "0" # agar sirf 0 aaya or hat gya lstrip k wjh se to res empty ho jayega to isi liye 0 return kr diye