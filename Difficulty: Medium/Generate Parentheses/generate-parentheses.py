class Solution:
    def solve(self, index, total, brackets, res):
        if index >= len(brackets):
            if total == 0:
                res.append("".join(brackets))
            return
        
        if total > len(brackets)//2:
            return
        elif total < 0:
            return
        brackets[index] = "("
        self.solve(index+1, total+1, brackets, res)
        brackets[index] = ")"
        self.solve(index+1, total-1, brackets, res)
        
    def generateParentheses(self, n: int) -> list[str]:
        res = []
        n = n//2
        brackets = [""] * (2*n)
        self.solve(0, 0, brackets, res)
        return res
