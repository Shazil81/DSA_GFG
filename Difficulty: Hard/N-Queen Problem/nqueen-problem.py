class Solution:
    def solve(self, row, board, ans, leftcol, upperDiagonal, lowerDiagonal, n):
            if row == n: 
                ans.append(board[:])  
                return
            for col in range(n):
                if (
                    leftcol[col] == 0
                    and lowerDiagonal[row + col] == 0
                    and upperDiagonal[n - 1 + col - row] == 0
                ):
                    board[row] = col + 1   
                    leftcol[col] = 1
                    lowerDiagonal[row + col] = 1
                    upperDiagonal[n - 1 + col - row] = 1

                    self.solve(row + 1, board, ans, leftcol, upperDiagonal, lowerDiagonal, n)

                    board[row] = 0   
                    leftcol[col] = 0
                    lowerDiagonal[row + col] = 0
                    upperDiagonal[n - 1 + col - row] = 0

    def nQueen(self, n: int) -> list[list[int]]:
        board = [0] * n
        ans = []
        leftcol = [0] * n
        upperDiagonal = [0] * (2 * n - 1)
        lowerDiagonal = [0] * (2 * n - 1)
        self.solve(0, board, ans, leftcol, upperDiagonal, lowerDiagonal, n)
        return ans
        