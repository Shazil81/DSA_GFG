class Solution:
    def canMakebouqets(self, bloomDay, m, k, days):
        bouquets = 0
        flowers = 0
        for bloom in bloomDay:
            if bloom <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        
        return bouquets >= m
    def minDaysBloom(self, arr, k, m):
        # Base Case
       if m * k > len(arr):
            return -1
       
       low = min(arr)
       high = max(arr)
       ans = -1

       while low <= high:
            mid = (low+high)//2 # mid as day
            if self.canMakebouqets(arr, m, k, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
       return ans
        
        