class Solution:
    def findCeil(self, arr, x):
        # Lower Bound hi lgega kyun ki pehla chhota element jo bada ya barabar ho
        low = 0
        high = len(arr) - 1
        ceil = -1
        
        while low <= high:
            mid = (low+high)//2
            if arr[mid] >= x:
                ceil = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ceil
                
