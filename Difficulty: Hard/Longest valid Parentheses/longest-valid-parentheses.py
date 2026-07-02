
class Solution:
    def maxLength(self, s):
        # Optimal approach bina stack k hai
        left = right = max_length = 0
    
        # 1. Left to Right pass
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_length = max(max_length, 2 * right)
            elif right > left:
                left = right = 0
                
        # 2. Right to Left pass
        left = right = 0
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_length = max(max_length, 2 * left)
            elif left > right:
                left = right = 0
                
        return max_length
        