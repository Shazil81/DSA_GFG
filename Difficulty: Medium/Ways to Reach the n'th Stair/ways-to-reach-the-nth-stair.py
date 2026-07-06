class Solution:
    def solve(self, index, dp):
        if index == 0 or index == 1:
            return 1
        
        if dp[index] !=-1:
            return dp[index]
        
        dp[index] = self.solve(index-1, dp) + self.solve(index-2, dp)
        return dp[index]
    def countWays(self, n: int) -> int:
        dp = [-1] * (n+1)
        
        return self.solve(n, dp)
        