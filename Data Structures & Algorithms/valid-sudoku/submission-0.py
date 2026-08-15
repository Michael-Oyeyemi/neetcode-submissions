from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[row])):
                square = (row // 3) * 3 + (col // 3)
                cell = board[row][col]
                if cell == '.':
                    continue
                if cell in rows[row] or cell in cols[col] or cell in squares[square]:
                    return False
                rows[row].add(cell)
                cols[col].add(cell)
                squares[square].add(cell)
        
        return True