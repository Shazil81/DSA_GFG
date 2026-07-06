class Solution:
    def func(self, i, j, m, n, dp):
        if i == 0 and j == 0: # base case hai jab last me phonch gye yaani ek route mila
            return 1
        if i < 0 or j < 0 or grid[i][j] == 1: #  agar boundary cross kr de tb
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        up = self.func(i-1, j, m, n, dp) # upward direction me jayega
        left = self.func(i, j-1, m, n, dp) # left direction me jayega

        dp[i][j] = up + left # dono ka sum hi hoga result
        return dp[i][j]
    def uniquePaths(self, grid):
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == 1:
            return 0
        dp = [[-1]*n for _ in range(m)] 
        return self.func(m-1, n-1, m, n, dp)
        