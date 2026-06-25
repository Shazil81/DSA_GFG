class Solution:
    def firstSearch(self, nums, target):
        # Iterative solution
        n = len(nums)
        low = 0
        high = n-1
        ans = -1
        while low<=high:
            mid = (low + high)//2
            if nums[mid] == target:
                ans = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return ans   
        