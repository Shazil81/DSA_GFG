class Solution:
    def findFloor(self, arr, x):
        # Ye lower Bound k Just opposite hai kyun ki element se chhota or wo largest hona chahiye
        lb = -1
        n = len(arr)
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            if arr[mid]<=x:
                lb = mid
                low = mid + 1
            else:
                high = mid - 1
        return lb
        