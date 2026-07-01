class Solution:
    def scoreOfParentheses(self, s):
        # Without using stack (Optimal)
        score = 0
        depth = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                # Agar ye ek valid pair '()' hai
                if s[i-1] == '(':
                    # Is pair ka contribution calculate karo: 2 power depth
                    score += pow(2, depth)
                    
        return score
        
        
        