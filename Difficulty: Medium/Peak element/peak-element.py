class Solution:   
    def peakElement(self, arr):
        # sorting Use nhi hoga kyun ki index change nhi krna hai
        n = len(arr)
        low = 0
        high = n - 1

        while low < high:
            mid = (low+high)//2
            if arr[mid] < arr[mid+1]:  # agar mid + 1 jayenge to low < high dena hoga
                low = mid + 1
            else:
                high = mid
        
        return low