class Solution:
    def reverse(self, n):
        rev = 0
        while n > 0:
            rev = rev * 10 + (n % 10)
            n //= 10
        
        return rev
    def reverseexponentiation(self, n):
        res = 1
        rev = self.reverse(n) # power
        while rev > 0:
            if rev % 2 == 1: # power odd alag se handle res se multiply number
                res = res * n
            
            n = n * n  # Number ka square
            rev = rev // 2 # power half
        
        return res
        