#!/usr/bin/python3
""" code that solves the n queen problem """
import sys


def is_safe(board, row, col, N):
    # Check if a queen can be placed at board[row][col]
    # horizontally and diagonally

    # Check the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(N):
    # Initialize an empty board
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(col):
        # Base case: If all queens are placed, save the solution
        if col >= N:
            solution = []
            for row in range(N):
                for col in range(N):
                    if board[row][col] == 1:
                        solution.append([row, col])
            solutions.append(solution)
            return True

        # Try placing a queen in each row of the current column
        for row in range(N):
            if is_safe(board, row, col, N):
                # Place the queen
                board[row][col] = 1

                # Recurse for the next column
                backtrack(col + 1)

                # Remove the queen (backtracking)
                board[row][col] = 0

        return False

    # Start the backtracking algorithm from the first column
    backtrack(0)

    # Print the solutions
    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
