class Solution: 
    def solve(self, index, arr, dp):
        if index == 0:
            return arr[index]
        if index < 0:
            return 0
        
        if dp[index] != -1:
            return dp[index]
        
        pick = arr[index] + self.solve(index-2, arr, dp)
        not_pick = 0 + self.solve(index-1, arr, dp)
        
        dp[index] = max(pick, not_pick)
        return dp[index]
        
    def findMaxSum(self, arr):
        n = len(arr)
        dp = [-1] * n
        return self.solve(n-1, arr, dp)
        