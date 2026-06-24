class Solution:
    def sort012(self, arr):
        # optimal solution with one pass (Dutch National Flag Algorithm)
        n = len(arr)
        low = 0
        mid = 0
        high = n - 1
        
        while mid <= high:
            # low ko 0 k liye use krenge
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            # mid ko 1 k liye rakhe hue h
            elif arr[mid] == 1:
                mid += 1
            # isme 2 k liye use hoga
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        return arr
        