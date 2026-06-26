class Solution:
    def searchInsertK(self, arr, k):
        # code here
        # This code is of lower bound but lb = len(nums) instead
        low = 0
        high = len(arr) -1
        lb = len(arr)
        while low <= high:
            mid = (low + high)//2
            if arr[mid] >= k:
                lb =  mid
                high = mid - 1
            else:
                low = mid + 1
        return lb