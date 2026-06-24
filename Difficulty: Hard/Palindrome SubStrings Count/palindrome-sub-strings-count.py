class Solution:
       
    def countPS(self, s):
        # Optimal approach
        n = len(s)
        total_count = 0 

        for i in range(0, n):
            # Odd length k liye
            left = i-1 # ye 3 length ka substring k liye use kr rhe hai
            right = i+1
            while left >= 0 and right < n and s[left] == s[right]:
                total_count += 1
                left -= 1
                right += 1
                
            left, right = i, i+1
            while left >= 0 and right < n and s[left] == s[right]:
                total_count += 1
                left -= 1
                right += 1
        
        return total_count
        