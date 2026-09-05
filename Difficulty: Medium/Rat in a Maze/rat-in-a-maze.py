class Solution:
    def solve(self, row, col, maze, n, ans, path):
        # base condition
        if row == n-1 and col == n-1:
            ans.append(path)
            return
        temp = maze[row][col]
        maze[row][col] = 0 # marking visited

        # Downward
        if row+1 < n and maze[row+1][col] == 1:
            self.solve(row+1, col, maze, n, ans, path+"D")
        # Left   
        if col -1 >= 0 and maze[row][col-1] == 1:
            self.solve(row, col-1, maze, n, ans, path+"L")
        # Right
        if col+1 < n and maze [row][col+1] == 1:
            self.solve(row, col+1, maze, n, ans, path+"R")
        # Upward
        if row-1 >= 0 and maze[row-1][col] == 1:
            self.solve(row-1, col, maze, n, ans, path+"U")
        # Backtrack k liye
        maze[row][col] = temp
            
    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        n = len(maze)
        # checking edge cases
        if maze[0][0] == 0 or maze[n-1][n-1] == 0:
            return []
        ans = []
        self.solve(0, 0, maze, n, ans, "")
        return ans
        