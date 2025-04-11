def is_safe(board, row, col, n):
    """
    Checks if placing a queen at board[row][col] is safe.
    """
    # Check the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n):
    """
    Solves the N-Queens problem using backtracking.
    """
    if row == n:  # All queens placed
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            if solve_n_queens(board, row + 1, n):  # Recur for the next row
                return True
            board[row][col] = 0  # Backtrack

    return False

def print_solution(board):
    """
    Prints the board configuration.
    """
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print("\n")

def n_queens(n):
    """
    Main function to solve the N-Queens problem.
    """
    board = [[0] * n for _ in range(n)]  # Initialize board
    if not solve_n_queens(board, 0, n):
        print("No solution exists!")
        return
    print_solution(board)

# Example usage
n = 8  # Change this for different board sizes
n_queens(n)
