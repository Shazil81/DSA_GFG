class Solution:
    def canPlace(self, stalls, n, cows, min_dist):
        count = 1
        last_pos = stalls[0]
        for i in range(1, n):
            if stalls[i] - last_pos >= min_dist:
                count += 1
            
                last_pos = stalls[i]
                
                if count >= cows:
                    return True
        
        return False
        
    def aggressiveCows(self, stalls, k):
        # Optimal Approach binary Search
        n = len(stalls)
        stalls.sort()
        low = 1
        high = stalls[-1] - stalls[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.canPlace(stalls, n, k, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
            
            
            
        