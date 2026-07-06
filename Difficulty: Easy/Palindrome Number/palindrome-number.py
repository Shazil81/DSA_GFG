class Solution:
    def isPalindrome(self, n):
		n = abs(n)  # Handle the negative sign as per platform requirement
        
        def reverse_number(num, rev):
            if num == 0:
                return rev
            return reverse_number(num // 10, (rev * 10) + (num % 10))
        
        return n == reverse_number(n, 0)
		    
		