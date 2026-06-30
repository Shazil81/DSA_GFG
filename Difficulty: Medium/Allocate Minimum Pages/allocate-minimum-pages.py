class Solution:
    def canPlace(self, arr, k, max_pages):
        count = 1
        curr_sum = 0
        for i in range(len(arr)):
            if curr_sum + arr[i] > max_pages:
                count += 1
                curr_sum = arr[i]
                if count > k:
                    return False
            else:
                curr_sum += arr[i]
        
        return True    
                
    def findPages(self, arr, k):
        n = len(arr)
        
        if k > n:
            return -1
        
        low = max(arr)
        high = sum(arr)
        ans = -1
        
        while low <= high:
            mid = (low+high)//2
            
            if self.canPlace(arr, k, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
        
        
