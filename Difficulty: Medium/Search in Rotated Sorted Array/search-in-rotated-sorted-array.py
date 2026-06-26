class Solution:
    def search(self, arr, key):
        # Optimal approach Binary Search
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low+high)//2
            if arr[mid] == key:
                return mid
            elif arr[mid] <= arr[high]:
                if arr[mid]<= key <= arr[high]:
                    low = mid+1
                else:
                    high = mid - 1
            else:
                if arr[low] <= key <= arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1
        