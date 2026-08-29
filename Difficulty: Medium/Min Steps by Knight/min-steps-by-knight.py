from collections import deque

class Solution:
	def minStepToReachTarget(self, knightPos, targetPos, n):
		# Bfs use hoga
		# Convert 1-based indexing to 0-based indexing
        start_x, start_y = knightPos[0] - 1, knightPos[1] - 1
        target_x, target_y = targetPos[0] - 1, targetPos[1] - 1
        
        # base case (already at target)
        if start_x == target_x and start_y == target_y:
            return 0
        
        # Queue stores (row, col, distance)
        queue = deque([(start_x, start_y, 0)])

        # Matrix to track visited cells
        visited = [[False] * n for _ in range(n)]
        visited[start_x][start_y] = True
        
        while queue:
            x, y, dist = queue.popleft()
            
            for dx, dy in [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)]:  # knight possible move
                nx, ny = x + dx, y + dy
                
                # Check if the move is valid and not yet visited
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if nx == target_x and ny == target_y:
                        return dist + 1

                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
        
        return -1
                
                
		