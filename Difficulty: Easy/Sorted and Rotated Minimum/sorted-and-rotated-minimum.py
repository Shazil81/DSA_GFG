class Solution:
    def findMin(self, arr):
        # Brute force linear search hoga
        # Optimal binary Search hoga
        low = 0
        high = len(arr)-1
        mini = float('inf')
        
        while low <= high:
            mid = (low+high)//2
            
            if arr[mid] <= arr[high]:
                mini = min(mini, arr[mid])
                high = mid - 1
            else:
                mini = min(mini, arr[low])
                low = mid + 1
        
        return mini
        