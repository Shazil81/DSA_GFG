class Solution:
    def searchMatrix(self, matrix, target): 
    	m = len(matrix) # rwos len
        n = len(matrix[0]) # col len
        low = 0
        high = m - 1
        row = -1
        # pehle find krenge kis row me hai me hai
        while low <= high:
            mid = (low + high) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][n-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                low = mid + 1
        if row == -1:
            return False
        
        # jo row aaya usme find krenge
        left = 0
        right = n - 1 # col len - 1

        while left <= right:
            mid = (left+right)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
    	
    	
