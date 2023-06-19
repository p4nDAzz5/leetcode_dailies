class Solution(object):
    def isValidSudoku(self, board):
        from collections import defaultdict
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = 9
        rowBoard = [[] for x in range(n)]
        colBoard = [[] for x in range(n)]
        boxBoard = defaultdict(set)

        for rows in range(len(board)):
            for cols in range(len(board[rows])):
                boxBoard[rows/3, cols/3] = set()
                if (board[rows][cols] in colBoard[cols] or board[rows][cols] in rowBoard[rows] or board[rows][cols] in boxBoard[rows] or board[rows][cols] in boxBoard[rows/3, cols/3]) and board[rows][cols].isdigit():
                    return False
                colBoard[cols].append(board[rows][cols])
                rowBoard[rows].append(board[rows][cols])
                boxBoard[rows/3, cols/3].add(board[rows][cols])

        return True