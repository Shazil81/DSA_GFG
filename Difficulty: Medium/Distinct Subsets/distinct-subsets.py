class Solution:
    def solve(self, index, nums, res, subset):
        res.append(subset.copy()) # ye if k bahar is liye hai kyun ki target hmlog ko match nhi krna h hmlog ko pura set chahiye isi liye bahar me bhi add kr rhe h
        if index >= len(nums): # base condition
            return
    
        for i in range(index, len(nums)): # combination sum II wala logic taaki duplicates remove ho jaye
            if i > index and nums[i] == nums[i-1]:
                continue
    
            subset.append(nums[i])
            self.solve(i+1, nums, res, subset)
            subset.pop()
        
    def findSubsets(self, arr):
        res = []
        arr.sort()
        self.solve(0, arr, res, [])
        return res
        
