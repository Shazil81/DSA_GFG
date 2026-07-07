class Solution:
    def solve(self, index, total, nums, dp):
        if index == 0:
            if total == 0 and nums[0] == 0:
                return 2
            if total == 0 or total == nums[0]:
                return 1
            return 0
        
        if dp[index][total] != -1:
            return dp[index][total]
        
        if nums[index] > total:
            pick = 0
        else:
            pick = self.solve(index-1, total-nums[index], nums,dp)
        not_pick = self.solve(index-1, total, nums, dp)
        
        dp[index][total] = pick + not_pick
        return dp[index][total]
                
	def perfectSum(self, arr, target):
		n = len(arr)
		dp = [[-1]*(target+1) for _ in range(n)]
		return self.solve(n-1, target, arr,dp)
		