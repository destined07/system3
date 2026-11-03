def is_safe(board, row, col, n):
    # Check the same column in earlier rows.
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal.
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal.
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_nqueens(board, row + 1, n):
                return True

            # Backtrack if this placement does not lead to a solution.
            board[row][col] = 0

    return False


n = int(input("Enter board size N (4 or more): "))

if n < 4:
    print("For this practical, enter N = 4 or greater.")
else:
    first_col = int(input("Enter column for the first queen (0 to " + str(n - 1) + "): "))

    if first_col < 0 or first_col >= n:
        print("Invalid column.")
    else:
        board = [[0 for j in range(n)] for i in range(n)]
        board[0][first_col] = 1

        if solve_nqueens(board, 1, n):
            print("\nOne solution (1 = queen, 0 = empty):")
            for row in board:
                print(row)
        else:
            print("No solution found with the first queen in that column.")
