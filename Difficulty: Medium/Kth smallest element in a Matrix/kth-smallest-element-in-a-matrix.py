class Solution:
    def solve(self, mat, n, target):
        count = 0
        row = n - 1
        col = 0
        
        while row >= 0 and col < n:
            if mat[row][col] <= target:
                count += (row + 1)
                col += 1
            else:
                row -= 1
        
        return count
        
    def kthSmallest(self, mat, k):
        # bottom left se start hoga
        n = len(mat)
        
        # 1. Binary search ka range set karo (sabse chota aur sabse bada element)
        low = mat[0][0]
        high = mat[n-1][n-1]
        ans = low
        
        # 2. Value-based binary search
        while low <= high:
            mid = (low + high) // 2
            
            # 3. Check karo ki 'mid' tak kitne elements matrix mein hain
            if self.solve(mat, n, mid) >= k:
                ans = mid       # 'mid' potential answer hai
                high = mid - 1  # Aur chota answer dhundne ki koshish karo
            else:
                low = mid + 1   # 'mid' chota hai, value badhao
        
        return ans
                
        