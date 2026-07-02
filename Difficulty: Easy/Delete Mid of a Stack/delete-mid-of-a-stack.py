class Solution:
    def solve(self, mid, index, stack):
        if index == mid:
            stack.pop()
            return
        temp = stack.pop()
        self.solve(mid, index+1, stack)
        stack.append(temp)
    def deleteMid(self, stack):
        #code here
        n = len(stack)
        mid = n//2
        self.solve(mid, 0, stack)
        return stack
        