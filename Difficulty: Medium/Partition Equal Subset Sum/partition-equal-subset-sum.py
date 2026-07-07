class Solution:
    def solve(self, index, total, nums, dp):
        # Base Case 1: Agar total 0 mil gaya, matlab partition mil gaya
        if total == 0:
            return True
        if index == 0:
            if nums[index] == total:
                return True
            return False
        if dp[index][total] != -1:
            return dp[index][total]
        if nums[index] > total:
            pick = False
        else:
            pick = self.solve(index-1, total-nums[index], nums, dp)
        
        not_pick = self.solve(index-1, total, nums, dp)

        dp[index][total] =  pick or not_pick
        return dp[index][total]
                
    def equalPartition(self, arr):
        n = len(arr)
        total = sum(arr)
        dp = [[-1]*(total//2 +1) for _ in range(n)]
        if total % 2 != 0: # partion hone k liye agar odd hai to ho nhi skta hai equal partition isi liye False
            return False
        return self.solve(n-1, total//2, arr, dp)
        