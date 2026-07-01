class Solution:
    def isBalanced(self, s):
        # Stack using
        
        stack = []
        for ch in s:
            if ch in ("({["):
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                bracket = stack.pop()
                
                if (ch == ')' and bracket == '(') or (ch == '}' and bracket == '{') or (ch == ']' and bracket == '['):
                    continue
                else:
                    return False
        
        return len(stack) == 0
        
        