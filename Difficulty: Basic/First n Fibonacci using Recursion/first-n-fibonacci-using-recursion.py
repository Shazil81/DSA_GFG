class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        res = []
        if n == 1: 
            return [0]
        if n == 2:
            return [0, 1]
        
        res = self.fibonacciNumbers(n-1)
        res.append(res[-1] + res[-2])
        return res
        