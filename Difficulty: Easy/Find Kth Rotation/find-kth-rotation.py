class Solution:
    def findKRotation(self, arr):
        # code here
        n = len(arr)
        for i in range(0, n-1):
            if arr[i+1] < arr[i]:
                return i+1
        
        return 0
                