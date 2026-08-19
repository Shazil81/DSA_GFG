class Solution:
    def solve(self, index, res, nums):
        # base case
        if index >= len(nums):
            res.append("".join(nums.copy()))
            return
        
        vis = set()
    
        for i in range(index, len(nums)):
            if nums[i] in vis:
                continue
            
            vis.add(nums[i])
            
            # Swap: Element ko correct position pe lao
            nums[index], nums[i] = nums[i], nums[index]
            # agle index k liye
            self.solve(index+1, res, nums)
            # Backtrack kro
            nums[index], nums[i] = nums[i], nums[index]
        
    def findPermutation(self, s: str) -> list[str]:
        res = []
        s = list(s)
        self.solve(0, res, s)
        return res
        
