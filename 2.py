def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col):
    # If all queens are placed then return true
    if col >= len(board):
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_n_queens_util(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution
            # then remove queen from board[i][col]
            board[i][col] = 0

    # If the queen cannot be placed in any row in this column col then return false
    return False

def solve_n_queens():
    board = [[0 for _ in range(8)] for _ in range(8)]
    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False

    print_board(board)
    return True

def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))

# Run the solver
solve_n_queens()
