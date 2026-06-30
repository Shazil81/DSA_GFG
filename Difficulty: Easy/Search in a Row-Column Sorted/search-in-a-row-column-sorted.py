class Solution:
	def matSearch(self, matrix, target):
		# Binary Search nhi lg skta hai
        m = len(matrix)
        n = len(matrix[0])

        rows, cols = 0, n - 1

        while rows < m and cols >= 0:
            if matrix[rows][cols] == target:
                return True
            elif matrix[rows][cols] > target:
                cols -= 1
            else:
                rows += 1
        
        return False

        # TC : O(m+n)